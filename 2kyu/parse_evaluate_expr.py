# https://www.codewars.com/kata/52a78825cdfc2cfc87000005

import operator
import regex as re

OP = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x-y,
    "*": lambda x, y: x*y,
    "/": lambda x, y: x/y
}


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def to_postfix(infix):
    stack = []
    ans = []
    print(infix.split())
    for sym in infix.split():
        if sym in '+-':
            if len(stack) != 0:
                while len(stack) != 0 and stack[-1] in '+-*/^':
                    ans += [stack.pop()]
            stack.append(sym)
        if sym in "*/":
            if len(stack) != 0:
                while len(stack) != 0 and stack[-1] in '*/^':
                    ans += [stack.pop()]
            stack.append(sym)
        if sym == '^':
            stack.append(sym)
        if sym == '(':
            stack.append(sym)
        if sym == ')':
            while stack[-1] != '(':
                ans += [stack.pop()]
            else:
                stack.pop()
        elif is_number(sym):
            ans += [sym]
        print(f'{ans=}')
        print(f'{stack=}')

    while len(stack) != 0:
        ans += [stack.pop()]
    print(ans)
    return ans


def postfix_evaluator(expr):
    stack = []
    for token in expr:
        if token in OP:
            b, a = stack.pop(), stack.pop()
            stack.append(OP[token](a, b))
        else:
            stack.append(float(token))
    return stack.pop()


def preprocess(expr):
    repl = [('* -', '* (-1)* '),
            ('/ -', '/ (-1)/'),
            ('+ -', ' - '),
            ('- -', ' + '),
            ('-(', '+ 0 - ('),
            ('(+', '('),
            ('(', '( '),
            (')', ' )')
            ]
    if expr.startswith('-'):
        expr = '(-1)*' + expr[1:]
    for r in repl:
        expr = expr.replace(r[0], r[1])
        print(expr)
    ans = ''
    for i, ch in enumerate(expr):
        if ch in '+-*/^' and expr[i-1] in '0123456789)':
            ans += f' {ch} '
        else:
            ans += ch

    return ans


def calc(expr):
    return postfix_evaluator(to_postfix(preprocess(expr)))
