"""
rectangle.py
------------

Implements the Rectangle class which inherits from Shape.
"""

from .abcShape import Shape


class Rectangle(Shape):
    """
    Rectangle defined by length and width.
    """

    def __init__(self, length: float, width: float):
        """
        :param length: positive float – the longer side
        :param width : positive float – the shorter side
        :raises ValueError: if any dimension is not positive
        """
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers.")
        self.length = length
        self.width = width

    # required implementations ------------------------------------------------
    def get_area(self) -> float:
        """Area = length × width."""
        return self.length * self.width

    def get_perimeter(self) -> float:
        """Perimeter = 2 × (length + width)."""
        return 2 * (self.length + self.width)
