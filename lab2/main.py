from lab_python_oop import circle, square, rect, color
from lab_python_oop.ac import GF
from loguru import logger
RED = color.Color("Red")
BLUE = color.Color("Blue")
GREEN = color.Color("Green")


def printfigure(figure: GF):
    print(f"{figure}\nArea is {figure.area()}")


if __name__ == "__main__":
    r = rect.Rect(25, 25, BLUE)
    printfigure(r)
    c = circle.Circle(25, GREEN)
    printfigure(c)
    s = square.Square(25, RED)
    printfigure(s)
    logger.debug("Hello, cool debugger")
# import abc
# class Food(abc.ABC):
#     @abc.abstractmethod
#     def cut(self):
#         pass
#
# class Meat(Food):
#     def cut(self):
#         pass
#
# class Apple(Food):
#     def cut(self):
#         pass
#
# class Bolt:
#     def no_cut(self):
#         pass
#
# def meatcutter(food: Food):
#     food.cut()