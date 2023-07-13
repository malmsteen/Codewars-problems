import math
from functools import lru_cache


@lru_cache(maxsize=None)
def exp_sum(n):

    if n == 0:
        return [[]]
    elif n == 1:
        return [[1]]
    s = 0
    dct = {}
    partitions = []
    for i in range(1, n+1):
        partitions += [[i] + v for v in exp_sum(n-i)]
        # print(partitions)
        s += len(exp_sum(n-i))
    tmp = set([tuple(sorted(p)) for p in partitions])
    return [list(t) for t in tmp]


for i in range(100):
    print(len(exp_sum(i)))
