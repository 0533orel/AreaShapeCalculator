"""
main.py  –  Area & Perimeter Calculator + Shape Operations
-----------------------------------------------------------
• Create shapes and store them in a list.
• Display the list of shapes created so far.
• Compare two shapes by their area  (==, <, >).
• Add or subtract the areas of two shapes and display the result.
"""

from shapes.rectangle      import Rectangle
from shapes.square         import Square
from shapes.triangle       import Triangle
from shapes.rightTriangle  import RightTriangle
from shapes.circle         import Circle
from shapes.regularHexagon import RegularHexagon
from typing import List

# ────────────────────────────────────────────────────────── helper functions

def positive_float(prompt: str) -> float:
    """Ask until the user enters a positive float."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Value must be positive – try again.")
                continue
            return value
        except ValueError:
            print("Input must be a number – try again.")


def build_triangle() -> object:
    """Sub-menu for triangle type; returns the shape object."""
    print("\nTriangle type:")
    print("  1. Right-angled triangle (base + height)")
    print("  2. General triangle (3 sides)")

    while True:
        t_choice = input("Enter 1 or 2: ").strip()
        try:
            if t_choice == "1":                         # Right-angled
                base   = positive_float("Enter base  : ")
                height = positive_float("Enter height: ")
                return RightTriangle(base, height)

            elif t_choice == "2":                       # General
                a = positive_float("Enter side a: ")
                b = positive_float("Enter side b: ")
                c = positive_float("Enter side c: ")
                return Triangle(a, b, c)

            else:
                print("Invalid option – choose 1 or 2.")
        except ValueError as e:
            print(f"Error: {e}")


def list_shapes(shapes: List[object]) -> None:
    """Print all shapes created so far with an index."""
    if not shapes:
        print("No shapes created yet.")
        return
    print("\nCurrent shapes:")
    for idx, shp in enumerate(shapes, start=1):
        print(f"[{idx}] {shp}")


def pick_two_indices(shapes: List[object]) -> tuple:
    """Ask the user to pick two valid indices and return the corresponding shapes."""
    while True:
        try:
            idx1 = int(input("First index : ")) - 1
            idx2 = int(input("Second index: ")) - 1
            if idx1 == idx2:
                print("Choose two different indices.")
                continue
            return shapes[idx1], shapes[idx2]
        except (ValueError, IndexError):
            print("Invalid indices – try again.")


# ────────────────────────────────────────────────────────── main loop

def menu() -> None:
    shapes: List[object] = []

    while True:
        print("\nMAIN MENU – choose an option:")
        print("1.  Create Rectangle")
        print("2.  Create Square")
        print("3.  Create Triangle")
        print("4.  Create Circle")
        print("5.  Create Regular Hexagon")
        print("6.  List shapes created so far")
        print("7.  Compare two shapes (==, <, >)")
        print("8.  Add / subtract areas of two shapes")
        print("9.  Exit")

        choice = input("Enter a number (1-9): ").strip()

        try:
            # ───── shape creation ─────
            if choice == "1":
                length = positive_float("Enter length: ")
                width  = positive_float("Enter width : ")
                shapes.append(Rectangle(length, width))

            elif choice == "2":
                side = positive_float("Enter side length: ")
                shapes.append(Square(side))

            elif choice == "3":
                shapes.append(build_triangle())

            elif choice == "4":
                radius = positive_float("Enter radius: ")
                shapes.append(Circle(radius))

            elif choice == "5":
                side = positive_float("Enter side length: ")
                shapes.append(RegularHexagon(side))

            # ───── utility options ─────
            elif choice == "6":
                list_shapes(shapes)

            elif choice == "7":
                list_shapes(shapes)
                if len(shapes) < 2:
                    continue
                s1, s2 = pick_two_indices(shapes)
                print(f"\nComparison by area:")
                print(f"  {s1.__class__.__name__} area = {s1.get_area():.2f}")
                print(f"  {s2.__class__.__name__} area = {s2.get_area():.2f}")
                print(f"  {s1.__class__.__name__} == {s2.__class__.__name__}?  {s1 == s2}")
                print(f"  {s1.__class__.__name__} <  {s2.__class__.__name__}?  {s1 <  s2}")
                print(f"  {s1.__class__.__name__} >  {s2.__class__.__name__}?  {s1 >  s2}")

            elif choice == "8":
                list_shapes(shapes)
                if len(shapes) < 2:
                    continue
                s1, s2 = pick_two_indices(shapes)
                print(f"\nArea math:")
                print(f"  {s1.__class__.__name__} + {s2.__class__.__name__} = {s1 + s2:.2f}")
                print(f"  {s1.__class__.__name__} - {s2.__class__.__name__} = {s1 - s2:.2f}")

            elif choice == "9":
                print("Goodbye!")
                break

            else:
                print("Invalid option – choose 1-9.")

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as ex:
            print(f"Unexpected error: {ex}")


if __name__ == "__main__":
    menu()
