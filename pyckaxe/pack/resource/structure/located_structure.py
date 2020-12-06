from pyckaxe.pack.resource.abc.located_resource import LocatedResource
from pyckaxe.pack.resource.structure.structure import Structure
from pyckaxe.pack.resource.structure.structure_location import StructureLocation


class LocatedStructure(LocatedResource[Structure, StructureLocation]):
    pass
