import itertools


# def next_bigger(n):
#     if len(set(str(n))) == 1:
#         return -1

#     strN = str(n)
# #     lst = list(itertools.permutations(strN))
# #     lst = set([''.join(tup) for tup in lst])
# #     lst = sorted(list(lst))
# #     idx = lst.index(strN)

# #     if n < 10 or len(set(strN)) == 1 or (idx + 1) == len(lst):
# #         return -1
# #     ans = int(lst[idx + 1])

#     lst = list(str(n))[::-1]
#     if len(lst) == 2:
#         if lst[0] > lst[1]:
#             return int(lst[0] + lst[1])
#         return -1

#     i = 0
#     while lst[i] <= lst[i+1]:
#         i += 1
#         if i == len(lst)-1:
#             return -1
#     # else:
#     #     lst[i], lst[i+1] = lst[i+1], lst[i]
#     #     if i == 0:
#     #         return int(''.join(lst[::-1]))

#     toSort = lst[:i+1]
#     t = lst[i+1]
#     rem = lst[i+2:]
#     nextTo_t = min([d for d in toSort if d > t])
#     idx = toSort.index(nextTo_t)
#     toSort.pop(idx)
#     toSort += [t]
#     toSort.sort(reverse=True)
#     ans = rem + [nextTo_t] + toSort

#     # ans = (srt+[digit]).sort(reverse=True) + [t] + lst[i+2:]

#     ans = ''.join(ans)
#     return int(ans)

def next_bigger(num):
    digits = [int(i) for i in str(num)]
    idx = len(digits) - 1
    while idx >= 1 and digits[idx-1] >= digits[idx]:
        idx -= 1
    if idx == 0:
        return -1
    pivot = digits[idx-1]
    swap_idx = len(digits) - 1
    while pivot >= digits[swap_idx]:
        swap_idx -= 1
    digits[swap_idx], digits[idx-1] = digits[idx-1], digits[swap_idx]
    digits[idx:] = digits[:idx-1:-1]
    return int(''.join(str(x) for x in digits))


print(next_bigger(12))
print(next_bigger(544))
print(next_bigger(21))
print(next_bigger(123))
print(next_bigger(144))
print(next_bigger(414))
print(next_bigger(123485321))
