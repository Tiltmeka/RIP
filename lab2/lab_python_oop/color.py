class Color:
    def __init__(self, color):
        self.color = color

    def check(self):
        print(self.color)
        return f"Color of this figure is {self.color}"

    def __str__(self):
        return self.color