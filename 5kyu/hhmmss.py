

def make_readable(seconds):
    hh = seconds // 3600
    mm = (seconds % 3600)//60
    ss = seconds % 60
    return f'{hh:02d}:{mm:02d}:{ss:02d}'
