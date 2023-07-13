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
    mm = seconds // 60
    hh = mm // 60
    dd = hh // 24
    yy = dd // 365

    times = [yy, dd, hh, mm, ss]
    durs = ['year', 'day', 'hour', 'minute', 'second']
#     punct = [ '' if t == 0 else ', ' ]
    ans = ''

    if len(times) == 1:
        idx = [i for i, e in enumerate(a) if e != 0]
        return format_period(times[idx], durs[idx])
    for t,d in zip(times[:-2], durs[:-2]):
        ans += f'{format_period(t, d)}, '
    ans += f'{format_period(times[-2], durs[-2])} '
    ans += f'and {format_period(times[-1], durs[-1])}'
