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


class Colors:
    WHITE = Color(255, 255, 255)
    BLACK = Color(0, 0, 0)
    GREEN = Color(34, 117, 76)
    GRAY = Color(195, 195, 195)
    RED = Color(237, 28, 36)
    BLUE = Color(0, 162, 232)
    YELLOW = Color(255, 242, 0)
    BROWN = Color(131, 81, 54)
