from shapes.rectangle import Rectangle
from shapes.square import Square
from shapes.triangle import Triangle
from shapes.circle import Circle
from shapes.hexagon import Hexagon

def menu():
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
            if choice == '1':
                length = float(input("Enter length: "))
                width  = float(input("Enter width : "))
                shape = Rectangle(length, width)

            elif choice == '2':
                side = float(input("Enter side length: "))
                shape = Square(side)

            elif choice == '3':
                base   = float(input("Enter base  : "))
                height = float(input("Enter height: "))
                shape = Triangle(base, height)

            elif choice == '4':
                radius = float(input("Enter radius: "))
                shape = Circle(radius)

            elif choice == '5':
                side = float(input("Enter side length: "))
                shape = Hexagon(side)

            elif choice == '6':
                print("Goodbye!")
                break

            else:
                print("Invalid option – please choose 1-6.")
                continue

            print(f"\n{shape}")

        except ValueError:
            print("Input must be a number – please try again.")

if __name__ == "__main__":
    menu()
