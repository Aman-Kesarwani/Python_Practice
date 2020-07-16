from collections import namedtuple


class Point:
    def __init__(self, x, y):
        self.xPos = x
        self.yPos = y

    def __eq__(self, other):
        return self.xPos == other.xPos and self.yPos == other.yPos


point_1 = Point(101, 202)
point_2 = Point(101, 202)

print(point_1 == point_2)  # magic method implemenation required for true

print(id(point_1))
print(id(point_2))

print("*************Simples Way**************")

Point_1 = namedtuple("Point", ["x", "y"])

p1 = Point_1(x=1, y=2)
# p1.x = 10 -- not possible to mutate
# p1 = Point(x=10, y=20) -- crete new object if differnt value required

p2 = Point_1(1, 2)
print(id(p1))
print(id(p2))

print(p1 == p2)  # magic method not required
