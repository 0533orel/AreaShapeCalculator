from .abcShape import Shape
from math import sqrt

class Triangle(Shape):
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("All sides must be positive.")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Triangle inequality violated.")
        self.a = a
        self.b = b
        self.c = c


    def get_area(self):
        s = (self.a + self.b + self.c) / 2
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def get_perimeter(self):
        return self.a + self.b + self.c
