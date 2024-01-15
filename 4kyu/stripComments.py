# https://www.codewars.com/kata/51c8e37cee245da6b40000bd

import regex as re


def solution(string, markers):

    strings = string.split('\n')
    for marker in markers:
        strings = [(s.strip() if marker not in s else s[:s.index(marker)].strip())
                   for s in strings]
    return '\n'.join(strings)
