# https://www.codewars.com/kata/52b7ed099cdc285c300001cd


def sum_of_intervals(intervals):
    lefts = [i[0] for i in intervals]
    rights = [i[1] for i in intervals]
    lefts.sort()
    rights.sort()

    in_flag = False
    i = 0
    j = 0
    balance = 0
    total_sum = 0
    begin = i
    n = len(lefts)
    while i < n:
        if balance == 0:
            begin = i
        while lefts[i] <= rights[j]:
            balance += 1
            if i + 1 != n:
                i += 1
                continue
        else:
            while j < n:
                balance -= 1
        if j + 1 != n:
            j += 1
        if balance == 0:
            end = j
            total_sum += rights[end] - lefts[begin]

    return total_sum


sum_of_intervals([(1, 5)])
sum_of_intervals([(1, 5), (6, 10)])
sum_of_intervals([(1, 5), (1, 5)])
sum_of_intervals([(1, 4), (7, 10), (3, 5)])
