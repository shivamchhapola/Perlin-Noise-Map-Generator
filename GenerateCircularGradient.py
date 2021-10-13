import numpy as np
import math


def generateCircularGradient(w, h, r):
    cgr = np.zeros((w, h))
    hw = int(w/2)
    hh = int(h/2)
    for i in range(w):
        for j in range(h):
            dw = abs(i - hw)
            dh = abs(j - hh)
            dis = math.sqrt(dw*dw + dh*dh)
            cgr[i][j] = dis
    maxcgr = np.amax(cgr)
    gradMax = r/maxcgr
    cgr = ((1 - cgr/maxcgr) - gradMax)
    for i in range(w):
        for j in range(h):
            if cgr[i][j] <= 0:
                cgr[i][j] = 0
    return cgr
