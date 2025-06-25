from rectangle import Rectangle

class Triangle(Rectangle):
    def __init__(self, base, height):
        super().__init__(base, height)

    def get_area(self):
        return (self.length * self.width) * 0.5

