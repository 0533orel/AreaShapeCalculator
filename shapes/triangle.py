"""
triangle.py
-----------

Implements a general triangle given its three sides
(using Heron's formula).
"""

from .abcShape import Shape
from math import sqrt


class Triangle(Shape):
    """
    General triangle defined by sides a, b, c.
    """

    def __init__(self, a: float, b: float, c: float):
        """
        Validates triangle inequality.

        :raises ValueError: if sides are non-positive or violate inequality.
        """
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("All sides must be positive.")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Triangle inequality violated.")
        self.a, self.b, self.c = a, b, c

    # required implementations ------------------------------------------------
    def get_area(self) -> float:
        """Area via Heron's formula."""
        s = (self.a + self.b + self.c) / 2  # semi-perimeter
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def get_perimeter(self) -> float:
        """Perimeter = a + b + c."""
        return self.a + self.b + self.c
