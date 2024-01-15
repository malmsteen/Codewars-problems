

import numpy as np


def rgb(r, g, b):
    # your code here :)

    r, g, b = np.clip([r, g, b], 0, 255)
    hx = [hex(color).split('x')[-1] for color in (r, g, b)]
    hx = ['0' + c if len(c) == 1 else c for c in hx]
    hexColor = ''.join(hx)

    return hexColor.upper()
