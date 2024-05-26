import math

class Hexagon(Figure):
    def __init__(self, color, side):
        super().__init__(color)
        self.side = side

    def perimetro(self):
        return 6 * self.side

    def area(self):
        return (3 * math.sqrt(3) * (self.side ** 2)) / 2
