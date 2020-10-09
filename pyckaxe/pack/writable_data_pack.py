from pyckaxe.pack.readable_data_pack import ReadableDataPack
from pyckaxe.pack.resource.abc.resource import Resource
from pyckaxe.pack.resource.abc.resource_location import ResourceLocation


class WritableDataPack(ReadableDataPack):
    async def write_resource(self, resource: Resource, resource_location: ResourceLocation):
        partial_path = resource_location.locate(self.context)
        await resource.dump(partial_path)
