# https: // www.codewars.com/kata/52685f7382004e774f0001f7


def make_readable(seconds):
    hrs = seconds // 3600
    mins = (seconds % 3600)//60
    secs = seconds % 60
    return f'{hrs:02d}:{mins:02d}:{secs:02d}'
