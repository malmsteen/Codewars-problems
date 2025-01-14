# https://www.codewars.com/kata/5426d7a2c2c7784365000783


def balanced_parens(n):
    def generate(p, left, right):
        if right >= left >= 0:
            if not right:
                yield p
            for q in generate(p + '(', left - 1, right):
                yield q
            for q in generate(p + ')', left, right - 1):
                yield q
    return list(generate('', n, n))
