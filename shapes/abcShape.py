"""
abcShape.py
-----------

Defines the abstract base class `Shape`, which all concrete
geometric shapes inherit from.  It enforces the implementation
of `get_area()` and `get_perimeter()` and provides common
dunder (magic) methods for printing, comparison and basic math.
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract base class for all 2-D shapes.

    Sub-classes *must* implement:
    • get_area()       – return the numeric area
    • get_perimeter()  – return the numeric perimeter
    """

    # ─────────────────────────── required API ────────────────────────────
    @abstractmethod
    def get_area(self) -> float:
        """Return the area of the shape (float)."""
        ...

    @abstractmethod
    def get_perimeter(self) -> float:
        """Return the perimeter / circumference of the shape (float)."""
        ...

    # ─────────────────────────── pretty printing ─────────────────────────
    def __str__(self):
        """Human-readable multi-line summary."""
        return (
            f"{self.__class__.__name__}:\n"
            f"  Area     : {self.get_area():.2f}\n"
            f"  Perimeter: {self.get_perimeter():.2f}"
        )

    def __repr__(self):
        """Debug-oriented single-line representation."""
        return (
            f"{self.__class__.__name__}"
            f"(area={self.get_area():.2f}, perimeter={self.get_perimeter():.2f})"
        )

    # ─────────────────────────── comparison operators ────────────────────
    def __eq__(self, other):
        """Shapes are equal if their areas are (almost) identical."""
        if isinstance(other, Shape):
            return abs(self.get_area() - other.get_area()) < 1e-6
        return NotImplemented

    def __lt__(self, other):
        """Smaller-than based on area."""
        if isinstance(other, Shape):
            return self.get_area() < other.get_area()
        return NotImplemented

    def __gt__(self, other):
        """Greater-than based on area."""
        if isinstance(other, Shape):
            return self.get_area() > other.get_area()
        return NotImplemented

    # ─────────────────────────── arithmetic operators ────────────────────
    def __add__(self, other):
        """Add the areas of two shapes (returns a float)."""
        if isinstance(other, Shape):
            return self.get_area() + other.get_area()
        return NotImplemented

    def __sub__(self, other):
        """Subtract the area of `other` from `self` (returns a float)."""
        if isinstance(other, Shape):
            return self.get_area() - other.get_area()
        return NotImplemented
