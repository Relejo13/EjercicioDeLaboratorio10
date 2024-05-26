import math

class Triangle(Figure):
    def __init__(self, color, side1, side2, side3):
        super().__init__(color)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimetro(self):
        return self.side1 + self.side2 + self.side3

    def area(self):
        s = self.perimetro() / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
