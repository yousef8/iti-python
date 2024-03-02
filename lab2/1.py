import math
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, name, color) -> None:
        if not isinstance(name, str) or not isinstance(color, str):
            raise ValueError("name and color must be string")
        self.name = name
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @abstractmethod
    def calculate_area():
        pass


class Circle(Shape):
    def __init__(self, name, color, radius) -> None:
        super().__init__(name, color)
        try:
            self.__radius = float(radius)
        except ValueError:
            raise ValueError("Radius must be a number")

    def calculate_area(self):
        return 0.5 * self.__radius * math.pi


class Square(Shape):
    def __init__(self, name, color, side) -> None:
        super().__init__(name, color)
        try:
            self.__side = float(side)
        except ValueError:
            raise ValueError("side must be a number")

    def calculate_area(self):
        return self.__side * self.__side


class Rectangle(Shape):
    def __init__(self, name, color, length, width) -> None:
        super().__init__(name, color)
        try:
            self.__length = float(length)
            self.__width = float(width)
        except ValueError:
            raise ValueError("length and width must be a number")

    def calculate_area(self):
        return self.__length * self.__width


circle = Circle("circle1", "red", 5.7)
square = Square("square1", "blue", 5)
rectangle = Rectangle("rectangle1", "green", 5, 5)

print(circle.calculate_area())
print(square.calculate_area())
print(rectangle.calculate_area())
