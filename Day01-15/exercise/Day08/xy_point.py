'''
定义一个类描述平面上的点
并提供移动点和计算到另一个点距离的方法。
Version: 0.1
Author: Cedar43
Date: 2019-12-08
'''
from math import sqrt


class xy_Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_2(self, a, b):
        self.x = a
        self.y = b

    def move(self, a, b):
        self.x += a
        self.y += b

    def distance(self, a, b):
        return sqrt((self.x - a)**2 + (self.y - b)**2)

    def get_xy(self):
        return (self.x, self.y)

    def __str__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))


def main():
    point_1 = xy_Point(1, 1)
    point_2 = xy_Point(2, 2)
    point_1.move_2(2, 3)
    print(point_1.get_xy())
    print(point_1)
    point_2.move(3, 4)
    print(point_2.get_xy())
    print(point_1.distance(2, 3), point_2.distance(5, 7))


if __name__ == "__main__":
    main()
