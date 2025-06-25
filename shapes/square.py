"""
square.py
---------

Square is a special case of Rectangle where all sides are equal.
"""

from .rectangle import Rectangle


class Square(Rectangle):
    """
    Square defined by a single side length.
    """

    def __init__(self, side: float):
        """
        :param side: positive float – length of each side
        """
        if side <= 0:
            raise ValueError("Side length must be positive.")
        super().__init__(side, side)

    def get_perimeter(self) -> float:
        """Perimeter = 4 × side."""
        return 4 * self.length
