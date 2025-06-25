from .rectangle import Rectangle
from math import sqrt

class RightTriangle(Rectangle):
    def __init__(self, base, height):
        super().__init__(base, height)

    def get_area(self):
        return (self.length * self.width) * 0.5

    def get_perimeter(self):
        hypotenuse = sqrt(self.length ** 2 + self.width ** 2)
        return self.length + self.width + hypotenuse