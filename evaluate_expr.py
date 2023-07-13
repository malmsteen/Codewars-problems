import unittest
import regex as re


def parse(expr):
    out = []
    if re.search('^-?\d+', expr):
        out.append(take_num(expr))
    if expr[0] in '+-*/':
        out.append(take_op(expr))
    return out


def take_num(expr):
    match = re.search('^-?\d+(\.\d+?\s*?)?', expr)
    num = match.group(0)
    expr = expr[match.end():]
    return num


def take_op(expr):
    op, expr = expr[0], expr[1:]
    return op


def calc(expr):
    expr = re.sub('(?=*|/\s*?)-(\d+|\(.*?\))', '(0- \1)', expr)
    expr = re.sub('(?<=\(|^)-', '0-', expr)
    expr = re.sub('(?<=*|/\s?)-', '0-', expr)
    stack = []
    while expr:
        parse(expr)

    return  # evaluated expression


cases = [("1 + 1", 2),
         ("8/16", 0.5),
         ("3 -(-1)", 4),
         ("2 + -2", 0),
         ("10- 2- -5", 13),
         ("(((10)))", 10),
         ("3 * 5", 15),
         ("-7 * -(6 / 3)", 14)]

for i, c in enumerate(cases[0:3]):
    print(i, calc(c[0]))
# for c in cases:
#     assert calc(c[0]) == c[1]
