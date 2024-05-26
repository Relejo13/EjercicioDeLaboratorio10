import math

class Circle(Figure):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def perimetro(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2
