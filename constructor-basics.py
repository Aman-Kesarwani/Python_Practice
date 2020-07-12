class Point:
    def __init__(self, x, y):  # self is reference to current obj
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
print(type(point))
print(isinstance(point, int))

print(point.x)
point.draw()
