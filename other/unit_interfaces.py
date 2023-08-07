import functools
import threading

from other.unit_parameters import Pair


class Physics:
    def __init__(self, coordinates: Pair, dimensions: Pair):
        self.coordinates = coordinates
        self.dimensions = dimensions


class Unit(Physics):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    worldSpeed = 3
    g = 0.5

    def __init__(self, x, y, width, height):
        Physics.__init__(self, Pair(x, y), Pair(width, height))

    def draw(self):
        self.updateShape()
        self.moveEngine()

    def updateShape(self):
        pass

    def moveEngine(self):
        self.coordinates.y += Unit.worldSpeed
