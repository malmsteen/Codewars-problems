# https://www.codewars.com/kata/55c6126177c9441a570000cc


def weight(st):
    return sum([int(d) for d in list(st)])


def order_weight(strng):

    stlst = strng.split()
    srt = sorted(stlst, key=weight)
    i = 0
    while i < len(srt[:-1]):
        if weight(srt[i]) != weight(srt[i+1]):
            i += 1
            continue
        else:
            begin = i
            while weight(srt[i]) == weight(srt[i+1]):
                i += 1
            else:
                last = i
            tmp = srt[begin:last+1]
            tmp.sort()
            srt[begin:last+1] = tmp

    return ' '.join(srt)


order_weight("103 123 4444 99 2000")
order_weight("2000 10003 1234000 44444444 9999 11 11 22 123")
print(order_weight(
    '1 2 200 4 4 6 6 7 7 9 27 72 18 81 91 425 31064 7920 67407 96488 34608557 71899703'))
