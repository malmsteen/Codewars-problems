# https://www.codewars.com/kata/54d496788776e49e6b00052f


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= abs(n):
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if abs(n) > 1:
        factors.append(abs(n))
    return factors


def sum_for_list(lst):

    divisors = [prime_factors(i) for i in lst]
    all_factors = set([fac for tup in divisors for fac in tup])

    out = []
    for f in all_factors:
        s = 0
        for i, tup in enumerate(divisors):
            if f in tup:
                s += lst[i]
        out.append([f, s])
        out.sort(key=lambda x: x[0])
    return out


a = [12, 15]
print(sum_for_list(a))
a = [15, 21, 24, 30, 45]
print(sum_for_list(a))
a = [15, 30, -45]
print(sum_for_list(a))
