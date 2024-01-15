# https://www.codewars.com/kata/5263c6999e0f40dee200059d


from functools import reduce


def get_pins(observed):
    dct = {
        1: [1, 4, 2],
        2: [2, 1, 3, 5],
        3: [3, 2, 6],
        4: [4, 1, 5, 7],
        5: [5, 4, 6, 2, 8],
        6: [6, 5, 3, 9],
        7: [7, 4, 8],
        8: [8, 7, 9, 5, 0],
        9: [9, 8, 6],
        0: [0, 8]
    }

    dct = {k: [str(n) for n in lst] for k, lst in dct.items()}
    digits = [int(d) for d in list(observed)]
    out = reduce(
        lambda x, y: [i + j for i in x for j in y], [dct[i] for i in digits])
    return out
