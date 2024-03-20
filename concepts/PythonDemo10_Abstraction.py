# This file gives demo about abstraction

from abc import ABC


class Shape(ABC):
    def draw(self):
        pass

    def show(self, shape_name=''):
        print(f"This is {shape_name} shape")


class TriangleShape(Shape):

    def __init__(self, shape_name="Triangle"):
        self.shapeName = shape_name

    def draw(self, a=0, b=0, c=0):
        print("Triagle[side1={}, side2={}, side3={}]".format(a, b, c))
        print("*"*50)


class RectangleShape(Shape):

    def __init__(self, shape_name="Rectangle"):
        self.shapeName = shape_name

    def draw(self, length=0, breadth=0):
        print("Rectangle[length={}, breadth={}".format(length, breadth))
        print("*"*50)


s1 = TriangleShape()
s2 = RectangleShape()

for s in [s1, s2]:
    s.show(s.shapeName)
    if isinstance(s, TriangleShape):
        s.draw(10, 20, 30)
    else:
        s.draw(15, 25)

