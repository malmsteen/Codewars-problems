# https://www.codewars.com/kata/534e01fbbb17187c7e0000c6


def lap(n):

    out = []
    if n == 1:
        return [(0, 0)], 0
    if n == 2:
        return [(0, 0), (0, 1), (1, 1)], 0

    i, j = [0, 0]
    for j in range(0, n):
        out.append((i, j))
    for i in range(1, n):
        out.append((i, j))
    for j in range(n-2, -1, -1):
        out.append((i, j))
    for i in range(n-2, 1, -1):
        out.append((i, j))

    n -= 4
    if n != 0:
        out.append((i, j+1))

    return out, n


def spiralize(size):
    n = size
    pairs = []
    while n > 0:
        k = (size - n)//2
        tmp, n = lap(n)
        pairs += [(k+i, k+j) for i, j in tmp]

    out = [[0] * size for _ in range(size)]
    for i, j in pairs:
        out[i][j] = 1
    return out
