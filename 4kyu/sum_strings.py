# https://www.codewars.com/kata/5324945e2ece5e1f32000370


import math


def sum_strings(x, y):
    a = [int(d) for d in str(x)][::-1] + [0]
    b = [int(d) for d in str(y)][::-1] + [0]
    diff = abs(len(x) - len(y))

    if len(a) > len(b):
        b = b + [0] * diff
    else:
        a = a + [0] * diff

    tmp = 0
    c = [0] * len(a)
    for i in range(len(a)):
        c[i] = (a[i] + b[i] + tmp) % 10
        tmp = (a[i] + b[i] + tmp) // 10

    ans = int(''.join([str(digit) for digit in c[::-1]]))

    return str(ans)


x = '523634637137'
y = '2636938261'
print(sum_strings(x, y))
