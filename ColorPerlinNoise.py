import numpy as np

lightblue = np.array([0, 191, 255])/255
blue = np.array([65, 105, 255])/255
green = np.array([34, 139, 34])/255
darkgreen = np.array([0, 100, 0])/255
sandy = np.array([210, 180, 140])/255
beach = np.array([238, 214, 175])/255
snow = np.array([255, 250, 250])/255
mountain = np.array([139, 137, 137])/255


def colorNoiseMap(wor, w, h):
    cwor = np.zeros((w, h)+(3,))
    for i in range(w):
        for j in range(h):
            if wor[i][j] < 0.37:
                cwor[i][j] = blue
            elif wor[i][j] < 0.39:
                cwor[i][j] = sandy
            elif wor[i][j] < 0.45:
                cwor[i][j] = beach
            elif wor[i][j] < 0.70:
                cwor[i][j] = green
            elif wor[i][j] < 0.77:
                cwor[i][j] = darkgreen
            elif wor[i][j] < 0.86:
                cwor[i][j] = mountain
            elif wor[i][j] <= 1.0:
                cwor[i][j] = snow
    return cwor
