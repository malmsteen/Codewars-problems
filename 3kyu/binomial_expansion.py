# https://www.codewars.com/kata/540d0fdd3b6532e5c3000b5b

from typing import *
import math
import regex as re


def parse(strng):
    binom, power = strng.split('^')
    var = re.search('[a-z]', binom).group(0)
    coefs = re.split('[a-z]', re.sub('\)|\(', '', binom))
    if coefs[0] == '':
        coefs[0] = 1
    return coefs, power, var


def full_coefs(c1: int, c2: int, power: int) -> List[int]:
    coefs = [math.comb(power, k) * c1**k * c2**(power - k)
             for k in range(power, -1, -1)]
    return coefs


def expand(expr):
    coefs, power, var = parse(expr)
    fc = full_coefs(int(coefs[0]), int(coefs[1]), int(power))

    out = ''
    for k, c in enumerate(fc):
        if c:
            sgn = '+' if c > 0 else ''
            out += f'{sgn}{str(c)}{var}^{int(power)-k}'
    out = re.sub('(?<=\d)[a-z]\^0', '', out)
    out = re.sub('\^1(?!=\d)', '', out)
    out = re.sub('(?<=\D)1(?=[a-z])', '', out)

    if out.startswith("+"):
        return out[1:]
    return out


binoms = ['(x+2)^1',
          '(x+2)^2',
          '(x+0)^2',
          '(0x+2)^2',
          '(2y +3)^3',
          '(x+1)^10',
          '(x-1)^10',
          '(2z -1)^6',
          '(-x + 2)^3'
          ]

for b in binoms:
    print(expand(b))
