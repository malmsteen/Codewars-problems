import string

s1, s2 = "Are they here", "yes, they are here"


def mix(s1, s2):
    s1 = ''.join(
        [s if s in string.ascii_lowercase else '' for s in s1.lower()])
    s2 = ''.join(
        [s if s in string.ascii_lowercase else '' for s in s2.lower()])

    d1 = dict()
    for letter in s1:
        d1[letter] = d1.get(letter, 0) + 1

    d2 = dict()
    for letter in s2:
        d2[letter] = d2.get(letter, 0) + 1

    allLetters = set(list(d1.keys()) + list(d2.keys()))
    outDict = dict()

    for letter in allLetters:
        n1, n2 = d1.get(letter, 0), d2.get(letter, 0)
        if n1 == n2 and n1 > 1:
            outDict[letter] = (0, n1)
            continue
        mx = max(n1, n2)
        if mx == 1:
            continue

        outDict[letter] = ([n1, n2].index(mx) + 1, mx)
    sortedD = sorted(outDict.items(), key=lambda item: item[1][1])
    outstr = ''.join([f'{v[0]}:{k*v[1]}/' if v[0] !=
                      0 else f'={k*v[1]}/' for k, v in sortedD.items()])

    return outstr


print(mix(s1, s2
          ))
