from math import sqrt
from .abcShape import Shape


class RegularHexagon(Shape):
    def __init__(self, length):
        if length <= 0:
            raise ValueError("Side length must be positive.")
        self.length = length

    def get_area(self):
        return (3 * sqrt(3) * (self.length ** 2)) / 2

    def get_perimeter(self):
        return 6 * self.length