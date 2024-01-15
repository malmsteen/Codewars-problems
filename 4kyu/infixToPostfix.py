# https://www.codewars.com/kata/52e864d1ffb6ac25db00017f


def to_postfix(infix):
    stack = []
    ans = ''
    for sym in infix:
        if sym.isdigit():
            ans += sym
        if sym in '+-':
            if len(stack) != 0:
                while len(stack) != 0 and stack[-1] in '+-*/^':
                    ans += stack.pop()
            stack.append(sym)
        if sym in "*/":
            if len(stack) != 0:
                while len(stack) != 0 and stack[-1] in '*/^':
                    ans += stack.pop()
            stack.append(sym)
        if sym == '^':
            stack.append(sym)
        if sym == '(':
            stack.append(sym)
        if sym == ')':
            while stack[-1] != '(':
                ans += stack.pop()
            else:
                stack.pop()

    while len(stack) != 0:
        ans += stack.pop()

    return ans
