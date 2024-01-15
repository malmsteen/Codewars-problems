# https://www.codewars.com/kata/53f40dff5f9d31b813000774


def recoverSecret(triplets):
    ans = ''

    l1, l2, l3 = [col for col in zip(*triplets)]

    while not all(letter == '' for letter in l1):
        for i, ch in enumerate(l1):
            if ch not in set(l2 + l3):
                triplets[i] = triplets[i][1:] + ['']
                if ch not in ans:
                    ans += ch
        l1, l2, l3 = [col for col in zip(*triplets)]

    return ans
