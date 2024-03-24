# This file gives demo about abstraction

from abc import ABC


class Shape(ABC):

    def __init__(self, shape_name=''):
        self.shapeName = shape_name

    def draw(self):
        pass

    def show(self):
        print(f"This is {self.shapeName} shape")


class TriangleShape(Shape):

    def __init__(self, a=0, b=0, c=0):
        super().__init__("Triangle")
        self.side1, self.side2, self.side3 = a, b, c

    def draw(self):
        print("{}[side1={}, side2={}, side3={}]"
              .format(self.shapeName, self.side1, self.side2, self.side3))
        print("*"*50)


class RectangleShape(Shape):

    def __init__(self, length=0, breadth=0):
        super().__init__("Rectangle")
        self.length_, self.breadth_ = length, breadth

    def draw(self, ):
        print("{}[length={}, breadth={}"
              .format(self.shapeName, self.length_, self.breadth_))
        print("*"*50)


s1 = TriangleShape(10, 20, 30)
s2 = RectangleShape(15, 25)

for s in [s1, s2]:
    s.show()
    s.draw()

