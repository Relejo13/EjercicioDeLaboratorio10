class Rectangle(Figure):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def perimetro(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height
