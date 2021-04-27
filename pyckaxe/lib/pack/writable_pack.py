from dataclasses import dataclass

from pyckaxe.lib.pack.physical_pack import PhysicalPack

__all__ = ("WritablePack",)


@dataclass
class WritablePack(PhysicalPack):
    """ A pack that has a physical, writable directory associated with it. """

    # TODO Idea: use __setitem__ with location as the key and resource as thr value.

    # DELETEME still used?
    # async def add(self, located_resource: LocatedResource, **options):
    #     partial_path = located_resource.location.resolve_path(self.context)
    #     await located_resource.resource.dump(partial_path, **options)
