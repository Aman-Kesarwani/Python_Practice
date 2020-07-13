class Point:
    def __init__(self, x, y):
        self.xPos = x
        self.yPos = y

    @classmethod
    def zero(cls):  # reference to class
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.xPos}, {self.yPos})")


#point = Point(15, 16)
point_1 = Point.zero()
point_1.draw()
