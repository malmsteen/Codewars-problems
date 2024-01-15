

def move_zeros(lst):

    zeros = []
    filtered = list(filter(lambda val: val != 0, lst))

    return filtered + [0]*(len(lst) - len(outlst))
