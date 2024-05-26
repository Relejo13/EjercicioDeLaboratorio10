from abc import ABC, abstractmethod

class Figure(ABC):
    def __init__(self, color):
        self.color = color

    def getColor(self):
        return self.color

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass
