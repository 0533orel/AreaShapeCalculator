"""
rightTriangle.py
----------------

Right-angled triangle (inherits Rectangle logic for legs).
"""

from .rectangle import Rectangle
from math import sqrt


class RightTriangle(Rectangle):
    """
    Right triangle defined by its two perpendicular legs
    (base = length, height = width).
    """

    def __init__(self, base: float, height: float):
        """
        :param base  : positive float – one leg
        :param height: positive float – the other leg
        """
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive.")
        super().__init__(base, height)

    # overrides ---------------------------------------------------------------
    def get_area(self) -> float:
        """Area = ½ · base · height."""
        return 0.5 * self.length * self.width

    def get_perimeter(self) -> float:
        """Perimeter = base + height + hypotenuse."""
        hypotenuse = sqrt(self.length ** 2 + self.width ** 2)
        return self.length + self.width + hypotenuse
