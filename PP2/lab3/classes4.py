from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, x, y):
        self.x, self.y = x, y

    def dist(self, other):
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

p1, p2 = Point(3, 4), Point(6, 8)
p1.show()
print(p1.dist(p2))