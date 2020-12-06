from pyckaxe.pack.readable_data_pack import ReadableDataPack
from pyckaxe.pack.resource.abc.located_resource import LocatedResource


class WritableDataPack(ReadableDataPack):
    async def add(self, located_resource: LocatedResource):
        partial_path = located_resource.location.resolve_path(self.context)
        await located_resource.resource.dump(partial_path)
