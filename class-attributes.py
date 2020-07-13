class Point:

    default_color = "orange"  # class level attributes shared accross all objects

    def __init__(self, x, y):  # self is reference to current obj
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


Point.default_color = "black"
point = Point(1, 2)
print(point.default_color)
print(Point.default_color)
point.z = 10  # can define object later also
point.draw()

another = Point(201, 202)
print(another.default_color)
another.draw()
