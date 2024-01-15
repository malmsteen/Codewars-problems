# https://www.codewars.com/kata/52b7ed099cdc285c300001cd


def sum_of_intervals(intervals):
    events = []
    events += [(i[0], 1) for i in intervals]
    events += [(i[1], -1) for i in intervals]
    events.sort()
    balance = 0
    l = 0
    for i, e in enumerate(events):
        if balance > 0:
            l += events[i][0] - events[i-1][0]
        if e[1] == 1:
            balance += 1
        else:
            balance -= 1
    return l
