from pyckaxe.safe_enum import SafeEnum


class StructureRotation(SafeEnum):
    none = "NONE"
    clockwise_90 = "CLOCKWISE_90"
    clockwise_180 = "CLOCKWISE_180"
    counterclockwise_90 = "COUNTERCLOCKWISE_90"
