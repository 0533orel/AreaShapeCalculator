# Shape Calculator

This project is a Python console-based **Area and Perimeter Calculator** for various geometric shapes. It allows users to:

- Create and store shape objects.
- List all created shapes with their properties.
- Compare shapes by area (`==`, `<`, `>`).
- Perform addition and subtraction operations on the areas of two shapes.

## Features

- Support for multiple shapes: Rectangle, Square, Triangle (including Right Triangle), Circle, and Regular Hexagon.
- Dynamic input validation and shape construction.
- Clear separation of concerns via object-oriented design.
- Operator overloading for area comparison and math operations.
- Rich menu-driven interface for ease of use.

---

## Project Structure

| File | Description |
|------|-------------|
| `main.py` | Entry point with the interactive menu. Manages user input and shape operations. |
| `abcShape.py` | Abstract base class (`Shape`) that defines required methods: `get_area`, `get_perimeter`, `__str__`, and magic methods for comparison and arithmetic. |
| `rectangle.py` | Implements `Rectangle` class (inherits from `Shape`) with area and perimeter logic. |
| `square.py` | Implements `Square` class, a specialized version of `Rectangle` with equal sides. |
| `triangle.py` | Implements `Triangle` class, which calculates area using Heron’s formula and includes validation for triangle inequality. |
| `rightTriangle.py` | Implements `RightTriangle` class, a subclass of `Rectangle`, and calculates area and perimeter using the Pythagorean theorem. |
| `circle.py` | Implements `Circle` class with radius-based area and perimeter formulas. |
| `regularHexagon.py` | Implements `RegularHexagon` class using standard geometric formulas for regular polygons. |

---

## How to Run

Make sure all files are in the same directory or inside a proper package folder (e.g., `shapes/`).

```bash
python main.py
```

---

## Requirements

- Python 3.7+
- No external libraries required (only standard library is used)

---

## Example Usage

```
MAIN MENU – choose an option:
1.  Create Rectangle
2.  Create Square
3.  Create Triangle
4.  Create Circle
5.  Create Regular Hexagon
6.  List shapes created so far
7.  Compare two shapes (==, <, >)
8.  Add / subtract areas of two shapes
9.  Exit
```

---

## License

This project is for educational purposes and is shared without a specific license.
