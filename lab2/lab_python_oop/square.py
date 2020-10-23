from lab_python_oop.rect import Rect


class Square(Rect):
    def __init__(self, a, color):
        self.a = a
        self.b = a
        self.color = color

    def __str__(self):
        return f"{self.color} colored square with {self.a} parameter "