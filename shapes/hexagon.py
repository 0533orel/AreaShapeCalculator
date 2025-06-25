from math import sqrt
from abcShape import Shape


class Hexagon(Shape):
    def __init__(self, length):
        self.length = length

    def get_area(self):
        return (3 * sqrt(3) * (self.length ** 2)) / 2
