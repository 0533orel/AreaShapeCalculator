"""
circle.py
---------

Implements a Circle with radius.
"""

from .abcShape import Shape
from math import pi


class Circle(Shape):
    """Circle defined by radius."""

    def __init__(self, radius: float):
        """
        :param radius: positive float
        """
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        self.radius = radius

    # required implementations ------------------------------------------------
    def get_area(self) -> float:
        """Area = π r²."""
        return (self.radius ** 2) * pi

    def get_perimeter(self) -> float:
        """Circumference = 2 π r."""
        return 2 * pi * self.radius
