# https://www.codewars.com/kata/53d40c1e2f13e331fc000c26


def fib_helper(n):
    if n == 0:
        return (0, 1)

    div, rem = divmod(n, 2)
    fibn, fibnp1 = fib_helper(div)

    fib2n = 2 * fibn * fibnp1 - fibn * fibn
    fib2np1 = fibn * fibn + fibnp1 * fibnp1

    if rem:
        return (fib2np1, fib2n + fib2np1)
    return (fib2n, fib2np1)


def fib(n):
    if n < 0:
        if n % 2 == 0:
            return -fib_helper(-n)[0]
        return fib_helper(-n)[0]
    return fib_helper(n)[0]
