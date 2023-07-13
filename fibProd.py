from typing import Generator
import math

# def fib(n: int) -> Generator[int, None, None]:
#     yield 0 # special case
#     if n > 0: yield 1 # special case
#     last: int = 0 # initially set to fib(0)
#     next: int = 1 # initially set to fib(1)
#     for _ in range(1, n):
#         last, next = next, last + next
#         yield next # main generation step


def fib5(n: int) -> int:
    if n == 0:
        return n  # special case
    lst: int = 0  # initially set to fib(0)
    nxt: int = 1  # initially set to fib(1)
    for _ in range(1, n):
        lst, nxt = nxt, lst + nxt
    return nxt


def productFib(prod):
    maxFeb = int(math.sqrt(prod))
    fibs = []
    n = 0
    while fib5(n) < maxFeb:
        #         fibs.append(f)
        n += 1
    a = fib5(n-1)
    b = fig5(n)
    if a*b == prod:
        return [a, b, True]
    elif a*b > prod:
        return [a, b, False]
    else:
        return [b, fib5(n+1), False]


productFib(4895)
