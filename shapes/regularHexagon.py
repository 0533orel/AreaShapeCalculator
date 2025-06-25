"""
regularHexagon.py
-----------------

Regular (equilateral) hexagon defined by side length.
"""

from math import sqrt
from .abcShape import Shape


class RegularHexagon(Shape):
    """
    Regular hexagon – all six sides are equal.
    """

    def __init__(self, length: float):
        """
        :param length: positive float – side length
        """
        if length <= 0:
            raise ValueError("Side length must be positive.")
        self.length = length

    # required implementations ------------------------------------------------
    def get_area(self) -> float:
        """Area = (3√3 / 2) · side²."""
        return (3 * sqrt(3) * (self.length ** 2)) / 2

    def get_perimeter(self) -> float:
        """Perimeter = 6 · side."""
        return 6 * self.length
