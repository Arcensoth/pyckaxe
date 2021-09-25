import asyncio
from dataclasses import dataclass, field
from datetime import datetime
from logging import Logger, getLogger
from typing import (
    Any,
    Callable,
    Coroutine,
    Dict,
    List,
    Optional,
    Set,
    Tuple,
    Type,
    TypeVar,
    cast,
)

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.abc.resource_scanner import ResourceScanner
from pyckaxe.lib.pack.physical_pack import PhysicalPack
from pyckaxe.lib.pack.physical_registry_location import PhysicalRegistryLocation
from pyckaxe.lib.pack.resource_cache_set import ResourceCacheSet
from pyckaxe.lib.pack.resource_processing_context import ResourceProcessingContext
from pyckaxe.lib.pack.resource_resolver_set import ResourceResolverSet
from pyckaxe.lib.pack.resource_transformer_set import ResourceTransformerSet
from pyckaxe.lib.pack.writable_pack import WritablePack
from pyckaxe.utils import walk_exception

__all__ = ("ResourceProcessingPipeline",)


DEFAULT = cast(Any, ...)

RT = TypeVar("RT", bound=Resource)


@dataclass
class _Result:
    scanner: ResourceScanner

    count_inputs: int = 0
    count_outputs: int = 0
    count_errors: int = 0
    errors: Set[Exception] = field(default_factory=lambda: set())

    def __str__(self) -> str:
        return str(self.scanner)


@dataclass
class ResourceProcessingPipeline:
    """
    Encapsulates everything needed to process and transform arbitrary resources.
    """

    input_pack: PhysicalPack
    output_pack: WritablePack
    scanner_factory: Callable[[PhysicalRegistryLocation, Type], ResourceScanner]
    caches: ResourceCacheSet
    resolvers: ResourceResolverSet
    transformers: ResourceTransformerSet
    match_files: Optional[str] = None

    log: Logger = field(init=False, default=DEFAULT)

    def __post_init__(self):
        self.log = getLogger(f"{self}")

    def __str__(self) -> str:
        return self.input_pack.name

    async def process(self, things: Dict[Type[Resource], Tuple[str, ...]]):
        self.log.info(f"Reading from: {self.input_pack.path}")
        self.log.info(f"Writing to: {self.output_pack.path}")

        # Create a separate task to process each registry.
        tasks: List[Coroutine[None, None, _Result]] = []
        for resource_type, parts in things.items():
            tasks_to_add = await self.collect_registry_tasks(resource_type, parts)
            tasks += tasks_to_add

        # Start the timer.
        time_start = datetime.utcnow()

        # Process registries asynchronously from one another.
        results = await asyncio.gather(*tasks)

        # Stop the timer.
        time_elapsed = datetime.utcnow() - time_start

        # Let the user know that processing is finished.
        self.log.info(f"Finished processing pipeline {self}")

        # Let the user know about any errors in each registry.
        for result in results:
            if result.errors:
                self.log.error(
                    f"Encountered {len(result.errors)} errors processing {result}:"
                )
                for i, error in enumerate(result.errors):
                    prefix = f"  [{i + 1}] "
                    pad = len(prefix) * " "
                    self.log.error(f"{prefix}{error}")
                    causes = list(walk_exception(error))
                    for cause in causes[:-1]:
                        self.log.error(f"{pad}├ {cause}")
                    self.log.error(f"{pad}└ {causes[-1]}")

        # Output some final metrics.
        self.log.info("Final cache status:")
        for resource_type, cache in self.caches.items():
            self.log.info(f"  - {resource_type.__name__}: {cache}")
        self.log.info(f"Time elapsed: {time_elapsed}")

    async def collect_registry_tasks(
        self, resource_type: Type[Resource], parts: Tuple[str, ...]
    ) -> List[Coroutine[None, None, _Result]]:
        self.log.info(f"Collecting {resource_type.__name__} registries:")
        registries = await self.input_pack.get_registries(*parts)
        tasks: List[Coroutine[None, None, _Result]] = []
        for registry in registries:
            self.log.info(f"  - {registry}")
            scanner = self.scanner_factory(registry, resource_type)
            task = self.process_registry(scanner)
            tasks.append(task)
        if not tasks:
            self.log.warning(f"No {resource_type.__name__} registries found")
        return tasks

    async def process_registry(self, scanner: ResourceScanner) -> _Result:
        self.log.info(f"Scanning {scanner}")
        result = _Result(scanner=scanner)
        async for input_location in scanner(match=self.match_files):
            self.log.debug(f"-> {input_location}")
            result.count_inputs += 1
            try:
                input_resource = await self.resolvers(input_location)
                ctx = ResourceProcessingContext[Any](
                    resolver_set=self.resolvers,
                    resource=input_resource,
                    location=input_location,
                )
                async for output_resource, output_location in self.transformers(ctx):
                    self.log.debug(f"  -> {output_location} (#{id(output_resource)})")
                    await self.output_pack.dump(output_resource, output_location)
                    result.count_outputs += 1
            except Exception as ex:
                self.log.exception(f"Error while processing resource {input_location}")
                result.errors.add(ex)
                result.count_errors += 1
        self.log.info(
            f"Finished scanning {scanner}"
            + (
                f" with {result.count_inputs} inputs -> {result.count_outputs} outputs"
                if result.count_inputs > 0
                else " (nothing to process)"
            )
            + (
                f" (with {result.count_errors} errors)"
                if result.count_errors > 0
                else ""
            )
        )
        return result
