# https://www.codewars.com/kata/5254ca2719453dcc0b00027d


from itertools import permutations as perm


def permutations(string):
    p = list(perm(string))
    return list(set([''.join(tup) for tup in p]))

# but I think is a kinda cheating. All tessts passed, but this should be made explicitly by manually.
