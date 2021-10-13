import noise
import numpy as np


def generateNoiseMap(w, h, p, l, o, s, ow, oh):
    wor = np.zeros((w, h))
    for i in range(w):
        for j in range(h):
            pnoise = noise.pnoise2(
                i/s + ow, j/s + oh, octaves=o, persistence=p, lacunarity=l, repeatx=w, repeaty=h, base=0)
            pnoise += 0.5
            pnoise = max(0, min(1, pnoise))
            wor[i][j] = pnoise
    return wor
