# https://www.codewars.com/kata/52a382ee44408cea2500074c


from itertools import permutations


def minor(matrix, x, y):
    """
    Get a remainder of the determinant
    """
    M_ans = []
    for row in range(len(matrix)):
        element_tmp = []
        if x == row:
            continue
        for column in range(len(matrix[row])):
            if y == column:
                continue
            element_tmp.append(matrix[row][column])
        M_ans.append(element_tmp)
    return M_ans


def prod(arr):
    p = 1
    for i in arr:
        p *= i
    return p


def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    det = 0
    for j in range(n):
        det += matrix[0][j] * (-1)**j * determinant(minor(matrix, 0, j))
    return det


m3 = [[2, 4, 2], [3, 1, 1], [1, 2, 0]]
m4 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
eye = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
print(determinant(m3))
print(determinant(m4))
print(determinant(eye))
