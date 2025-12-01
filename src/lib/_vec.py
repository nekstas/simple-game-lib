from __future__ import annotations


class Vec:
    _x: int
    _y: int

    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.__class__.__name__}(x={self.x}, y={self.y})'

    def __repr__(self):
        return str(self)

    def __eq__(self, other: Vec):
        import src.lib._asserts as _asserts
        _asserts.assert_vector(other)

        return (self.x, self.y) == (other.x, other.y)

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __neq__(self, other: Vec):
        return not (self == other)

    def __pos__(self):
        return Vec(self.x, self.y)

    def __neg__(self):
        return Vec(-self.x, -self.y)

    def __add__(self, other: Vec) -> Vec:
        import src.lib._asserts as _asserts
        _asserts.assert_vector(other)

        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vec) -> Vec:
        import src.lib._asserts as _asserts
        _asserts.assert_vector(other)

        return Vec(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int) -> Vec:
        import src.lib._asserts as _asserts

        _asserts.assert_vector_coord(other)
        return Vec(self.x * other, self.y * other)

    def __rmul__(self, other: int) -> Vec:
        import src.lib._asserts as _asserts

        _asserts.assert_vector_coord(other)
        return Vec(self.x * other, self.y * other)

    def __floordiv__(self, other: int) -> Vec:
        import src.lib._asserts as _asserts

        _asserts.assert_vector_coord(other)
        assert other != 0, 'Нельзя делить на 0.'

        return Vec(self.x // other, self.y // other)

    def __mod__(self, other: Vec) -> Vec:
        import src.lib._asserts as _asserts
        _asserts.assert_vector(other)
        assert other != Vec(0, 0), 'Нельзя делить с остатком на 0.'

        return Vec(self.x % other.x, self.y % other.y)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x: int):
        import src.lib._asserts as _asserts
        _asserts.assert_vector_coord(x)
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y: int):
        import src.lib._asserts as _asserts
        _asserts.assert_vector_coord(y)
        self._y = y
