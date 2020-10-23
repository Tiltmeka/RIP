from lab_python_oop.ac import GF
from math import pi


class Circle(GF):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def area(self):
       return self.radius * self.radius * pi

    def __str__(self):
        return f"{self.color} colored circle with {self.radius} radius "