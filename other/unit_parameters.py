class Pair:
    def __init__(self, _x: int, _y: int):
        self._x = _x
        self._y = _y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value: int):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value: int):
        self._y = value

    def get(self):
        return self.x, self.y


class Color:
    def __init__(self, _r, _g, _b):
        self._r = _r
        self._g = _g
        self._b = _b

    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, value):
        self._r = value

    @property
    def g(self):
        return self._g

    @g.setter
    def g(self, value):
        self._g = value

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        self._b = value

    def get(self):
        return self.r, self.g, self.b


class KeyMatrix:
    def __init__(self):
        self._down = False
        self._up = False
        self._left = False
        self._right = False
        self._space = False

    @property
    def down(self):
        return self._down

    @down.setter
    def down(self, value):
        self._down = value

    @property
    def up(self):
        return self._up

    @up.setter
    def up(self, value):
        self._up = value

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, value):
        self._left = value

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, value):
        self._right = value

    @property
    def space(self):
        return self._space

    @space.setter
    def space(self, value):
        self._space = value
