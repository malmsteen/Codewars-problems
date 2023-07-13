from itertools import permutations


def minor(matrix, x_index, y_index):
    """
    Get a remainder of the determinant
    """
    M_ans = []
    for row in range(len(matrix)):
        element_tmp = []
        if x_index == row:
            continue
        for column in range(len(matrix[row])):
            if y_index == column:
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
        # print(f"{matrix=}, {j=}")
#     perms = permutations(range(n))

#     det = 0
#     for idx, p in enumerate(perms):
#         det +=  (-1)**idx * prod([matrix[i][j] for i,j in zip(range(n), p)])
    return det


m5 = [[2, 4, 2], [3, 1, 1], [1, 2, 0]]
print(determinant(m5))
