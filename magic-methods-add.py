class Point:
    def __init__(self, x, y):
        self.xPos = x
        self.yPos = y

    def __add__(self, other):
        return Point(self.xPos + other.xPos, self.yPos + other.yPos)


point = Point(101, 201)
other = Point(301, 401)
combined = point + other
print(f"xPos: {combined.xPos}, yPos: {combined.yPos}")
