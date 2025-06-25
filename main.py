"""
main.py – Area & Perimeter Calculator
------------------------------------
Run this file to interactively calculate the area and perimeter of
rectangles, squares, triangles (right-angled or general), circles
and regular hexagons.
"""

from shapes.rectangle import Rectangle
from shapes.square import Square
from shapes.triangle import Triangle            # general triangle (3 sides)
from shapes.rightTriangle import RightTriangle  # right-angled triangle
from shapes.circle import Circle
from shapes.regularHexagon import RegularHexagon


def positive_float(user_input: str):
    """Helper that keeps asking until the user enters a positive float."""
    while True:
        try:
            value = float(input(user_input))
            if value <= 0:
                print("Value must be positive – try again.")
                continue
            return value
        except ValueError:
            print("Input must be a number – try again.")


def build_triangle():
    """Sub-menu for choosing triangle type and returning the shape object."""
    print("\nTriangle type:")
    print("  1. Right-angled triangle (base + height)")
    print("  2. General triangle (3 sides)")

    while True:
        t_choice = input("Enter 1 or 2: ").strip()
        try:
            if t_choice == "1":                        # Right-angled
                base   = positive_float("Enter base  : ")
                height = positive_float("Enter height: ")
                return RightTriangle(base, height)

            elif t_choice == "2":                      # General
                a = positive_float("Enter side a: ")
                b = positive_float("Enter side b: ")
                c = positive_float("Enter side c: ")
                return Triangle(a, b, c)

            else:
                print("Invalid option – please choose 1 or 2.")
        except ValueError as e:                         # from Shape ctor
            print(f"Error: {e}")


def menu() -> None:
    """Main interactive loop."""
    while True:
        print("\nChoose a shape to calculate its area and perimeter:")
        print("1. Rectangle")
        print("2. Square")
        print("3. Triangle")
        print("4. Circle")
        print("5. Regular Hexagon")
        print("6. Exit")

        choice = input("Enter a number (1-6): ").strip()

        try:
            if choice == "1":
                length = positive_float("Enter length: ")
                width  = positive_float("Enter width : ")
                shape = Rectangle(length, width)

            elif choice == "2":
                side = positive_float("Enter side length: ")
                shape = Square(side)

            elif choice == "3":
                shape = build_triangle()

            elif choice == "4":
                radius = positive_float("Enter radius: ")
                shape = Circle(radius)

            elif choice == "5":
                side = positive_float("Enter side length: ")
                shape = RegularHexagon(side)

            elif choice == "6":
                print("Goodbye!")
                break

            else:
                print("Invalid option – please choose 1-6.")
                continue

            print(f"\n{shape}")  # uses Shape.__str__()

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as ex:
            print(f"Unexpected error: {ex}")


if __name__ == "__main__":
    menu()
