class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str(f"({self.x},{self.y})")

    def __repr__(self):
        return str(self)

    @property
    def is_origin(self):
        if self.x == 0 and self.y == 0:
            return True

        return False


class Triangle(object):
    def __init__(self, points_string):
        nums = [int(i) for i in points_string.split(',')]
        self.p1 = Point(*nums[:2])
        self.p2 = Point(*nums[2:4])
        self.p3 = Point(*nums[4:])

        self.points = [self.p1, self.p2, self.p3]

        if any([p.is_origin for p in self.points]):
            print("ORIGIN WAS A POINT PROVIDED!")

    @property
    def area(self):
        return self.shoelace(*self.points)

    @property
    def contains_origin(self):
        origin = Point(0,0)

        a1 = self.shoelace(self.p1, self.p2, origin)
        a2 = self.shoelace(self.p1, self.p3, origin)
        a3 = self.shoelace(self.p2, self.p3, origin)

        if a1 + a2 + a3 == self.area:
            return True

        return False

    @staticmethod
    def shoelace(p1, p2, p3):
        """
        Shoelace Formula to find area of triangle defined by 3 points
        """
        return 0.5 * abs((p1.x - p3.x) * (p2.y - p1.y) - (p1.x - p2.x) * (p3.y - p1.y))


if __name__ == '__main__':
    count = 0
    with open("resources/p102_triangles.txt") as f:
        for t_string in f:
            tri = Triangle(t_string)
            if tri.contains_origin:
                count += 1

    print(count)
