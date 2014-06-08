import math


def distance(pt1, pt2):
    x1, y1 = pt1
    x2, y2 = pt2
    return math.hypot(x2 - x1, y2 - y1)

from functools import partial
points = [(1, 2), (3, 4), (5, 6), (7, 8)]
pt = (4, 3)
points.sort(key=partial(distance, pt))

print(points)
