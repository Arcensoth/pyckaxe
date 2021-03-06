import numpy as np

class Base:
    def snbt(self) -> str: ...

class End(Base): ...
class Numeric(Base): ...
class NumericInteger(Numeric, int): ...
class Byte(NumericInteger): ...
class Short(NumericInteger): ...
class Int(NumericInteger): ...
class Long(NumericInteger): ...
class Float(Numeric, float): ...
class Double(Numeric, float): ...
class Array(Base, np.ndarray): ...
class ByteArray(Array): ...
class String(Base, str): ...
class List(Base, list): ...
class Compound(Base, dict): ...
class IntArray(Array): ...
class LongArray(Array): ...
