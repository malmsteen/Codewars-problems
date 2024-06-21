# https://www.codewars.com/kata/52742f58faf5485cae000b9a

def format_period(n, dur):
    if n == 0:
        return ''
    elif n == 1:
        return f'{n} {dur}'
    else:
        return f'{n} {dur}s'


def format_duration(seconds):

    if seconds == 0:
        return 'now'

    ss = seconds % 60
    mm = seconds // 60 % 60
    hh = seconds // 3600 % 24
    dd = seconds // 3600 // 24 % 365
    yy = seconds // 3600 // 24 // 365
    times = [yy, dd, hh, mm, ss]
    durs = ['year', 'day', 'hour', 'minute', 'second']
    ans = ''

    for t, d in zip(times, durs):
        ans += f'{format_period(t,d)}'

    splitted = [s for s in ans.split(', ') if s != '']
    if len(splitted) == 1:
        return splitted[0]

    ans = ', '.join(splitted[:-1]) + f' and {splitted[-1]}'
    return ans
