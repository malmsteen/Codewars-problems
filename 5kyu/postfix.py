def to_postfix (infix):
    stack = []
    ans = ''
    for sym in infix:
        if sym.isdigit():
            ans += sym
        if sym in '+-':
            if len(stack) != 0:
                while len(stack) !=0 and stack[-1] in '+-*/^':
                    ans += stack.pop()
            stack.append(sym)
        if sym in "*/":
            if len(stack) != 0:
                while len(stack) !=0 and stack[-1] in '*/^':
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

print(to_postfix("2+7*5") == "275*+")
print(to_postfix("3*3/(7+1)") == "33*71+/")
print(to_postfix("5+(6-2)*9+3^(7-1)") == "562-9*+371-^+")
print(to_postfix("(5-4-1)+9/5/2-7/1/7") == "54-1-95/2/+71/7/-")
print(to_postfix("1^2^3") == "123^^")
