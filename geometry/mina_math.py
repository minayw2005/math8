import math


def distance(x1, y1, x2, y2):
    d_x = (x2 - x1) ** 2
    d_y = (y2 - y1) ** 2
    d = math.sqrt(d_x + d_y)

    return d


def slope(x1, y1, x2, y2):
    d_y = (y2 - y1)
    d_x = (x2 - x1)

    return d_y / d_x
