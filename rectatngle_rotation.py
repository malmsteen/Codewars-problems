import math


def rectangle_rotation(a, b):
    l1 = int(a/2/math.sqrt(2)) * 2
    l2 = int(b/2/math.sqrt(2)) * 2

    out = (l1 + 1) * (l2 + 1) + l1 * l2
    return out - 1 if out % 2 == 0 else out


print(rectangle_rotation(8, 6))
