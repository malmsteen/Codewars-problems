import regex as re


def parse(p):
    p = re.sub('\s+', '', p)
    if p.isdigit() or p.startswith('-') and p[1:].isdigit():
        return [int(p)]
    if p[0] not in '+-':
        p = '+' + p
    var = re.search('[a-zA-Z]', p).group(0)
    p = re.sub(f'({var})(?!\^)', r'\1^1', p)
    p = re.sub(f'(?<!\^|\d)(\d+)(?!\d*[a-z])', fr'\1{var}^0', p)
    p = re.split('(?=\+|-)', p)
    p = [m for m in p if m != '']
    p.sort(key=lambda x: re.split('\^', x)[-1], reverse=True)
    p = ''.join(p)

    coefs = []
    for s in re.split('[a-z]\^\d+', p):
        if s == '+':
            coefs.append('+1')
        elif s == '-':
            coefs.append('-1')
        elif s != '':
            coefs.append(s)
    powers = re.findall('(?<=\^)\d+', p)
    powers = [int(pwr) for pwr in powers]
    out = []
    for i, v in enumerate(range(powers[0], -1, -1)):
        if v in powers:
            out.append(coefs.pop(0))
        else:
            out.append(0)

    return [int(o) for o in out]


def convolution(s1, s2):
    res = [0]*(len(s1)+len(s2)-1)
    for o1, i1 in enumerate(s1):
        for o2, i2 in enumerate(s2):
            res[o1+o2] += i1*i2
    return res


def polynomial_product(p1: str, p2: str) -> str:
    try:
        var = re.search('[a-zA-Z]', p1 + p2).group(0)
    except:
        return str(int(p1) * int(p2))

    coefs1 = parse(p1)
    coefs2 = parse(p2)
    if coefs1 == [0] or coefs2 == [0]:
        return '0'
    conv = convolution(coefs1, coefs2)
    l = len(conv)
    out = ''
    for i, c in enumerate(conv):
        if c != 0:
            out += f"{'+'*(c>0)}{c}{var}^{l - (i+1)}"

    out = re.sub(fr'({var}\^0)|(^\+)', '', out)
    out = re.sub('^1(?!\d)')
    out = re.sub(f'1(?={var})', '', out)

    return out


p1 = "2u +u^2 +1"
p2 = "u + 1"
# print(parse())
t1 = "0"
t2 = "2 - x"
p1 = "4s^2 - 1"
p2 = "4s^2 + 1"
p1, p2 = "27a^3 - 27a^2 + 9a^1 - 1", "3a + 1"
p1, p2 = "F + 1", "F - 1"
p1, p2 = "L^2 - 3L + 1", "4L - 2"
p1, p2 = "-10i^13 - i + 152i^101", "-3 -98i^34 + 7i^2 - 4i"
print(polynomial_product(p1, p2))
# print(parse('x^2'))
