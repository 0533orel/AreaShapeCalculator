from .rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side):
        if side <= 0:
            raise ValueError("Side length must be positive.")
        super().__init__(side, side)

    def get_perimeter(self):
        return 4 * self.length
