# https://www.codewars.com/kata/52ec24228a515e620b0005ef

def gen5(n):
    k = 1
    while True:
        p = (3*k**2 - k)//2
        if p <= n:
            yield (-1)**(k - 1 % 2), p
        else:
            break
        q = (3*k**2+k)//2
        if q <= n:
            yield (-1)**(k - 1 % 2), q
        else:
            break
        k += 1


def exp_sum(n):
    p = [1]
    for i in range(1, n+1):
        p.append(sum(sgn * p[i-k] for sgn, k in gen5(i)))

    return p[-1]


print(exp_sum(10000))
