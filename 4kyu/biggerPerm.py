# https://www.codewars.com/kata/55983863da40caa2c900004e/python
# Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:

#   12 ==> 21
#  513 ==> 531
# 2017 ==> 2071
# If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift, None in Rust):

#   9 ==> -1
# 111 ==> -1
# 531 ==> -1


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


data = [12, 544, 21, 123, 144, 414, 123485321]
for d in data:
    print(next_bigger(d))
