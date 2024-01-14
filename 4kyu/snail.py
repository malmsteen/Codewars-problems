# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1


def lap(square):
    n = len(square)

    out = []

    if square == []:
        return [], []
    if len(square[0]) == 1:
        return square[0], []

    i, j = [0, 0]
    for j in range(0, n):
        out.append(square[i][j])
    for i in range(1, n):
        out.append(square[i][j])
    for j in range(n-2, -1, -1):
        out.append(square[i][j])
    for i in range(n-2, 0, -1):
        out.append(square[i][j])

    square = [row[1:-1] for row in square[1:-1]]
    return out, square


def snail(square):
    n = len(square)

    out = []
    while len(square) > 0:
        tmp, square = lap(square)
        out += tmp

    return out


array1 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
array2 = [[1,  2,  3,   4],
          [5,  6,  7,   8],
          [9, 10, 11,  12],
          [13, 14, 15, 16]]
print(snail(array1))
print(snail(array2))
