class Point:
    def __init__(self, x, y):
        self.xPos = x
        self.yPos = y

    def __eq__(self, other):
        return self.xPos == other.xPos and self.yPos == other.yPos

    def __gt__(self, other):
        return self.xPos > other.xPos and self.yPos > other.yPos


point = Point(18, 19)
point_1 = Point(16, 17)

print(point == point_1)
print(point < point_1)
