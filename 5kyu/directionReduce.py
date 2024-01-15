# https://www.codewars.com/kata/550f22f4d758534c1100025a

import regex as re

a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]


def dirReduc(arr):

    lst = ' '.join(arr)

    opp1 = ["NORTH", "SOUTH"]
    opp2 = ["EAST", "WEST"]

    to_cancel = [' '.join(opp1), ' '.join(opp1[::-1]),
                 ' '.join(opp2), ' '.join(opp2[::-1])]

    flag = True
    while flag:
        for l in to_cancel:
            lst = re.sub(l, '', lst)
            lst = re.sub(' {2,}', ' ', lst.strip())

        flag = any([bool(re.search(seq, lst)) for seq in to_cancel])

    return lst.split()


print(dirReduc(a))
