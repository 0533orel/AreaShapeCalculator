from abcShape import Shape
from math import pi

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return (self.radius**2) * pi

    def get_perimeter(self):
        return 2 * pi * self.radius