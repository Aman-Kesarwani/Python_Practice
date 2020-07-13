class Point:
    def __init__(self, x, y):
        self.xPos = x
        self.yPos = y

    def draw(self):
        print(f"Point ({self.xPos}, {self.yPos})")

    def __str__(self):
        return f"({self.xPos}, {self.yPos})"


point = Point(15, 16)

print(point)
print(str(point))
