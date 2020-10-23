from lab_python_oop.ac import GF


class Rect(GF):
    def __init__(self, a, b, color):
        self.a = a
        self.b = b
        self.color = color

    def area(self):
        return self.a * self.b

    def __str__(self):
        return f"{self.color} colored rectangle with {self.a} and {self.b} parameters "