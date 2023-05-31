import numpy as np
import matplotlib.pyplot as plt


def linearRegression(X, Y):
    n = X.shape[0]
    a = 1
    b = 2

    Sxy = 0
    Sx = 0
    Sy = 0
    Sxx = 0

    for i in range(n):
        Sx += (X[i])
        Sy += (Y[i])
        Sxy += (X[i]*Y[i])
        Sxx += (X[i]*X[i])

    b = ((n*Sxy) - (Sx * Sy)) / ((n*Sxx) - (Sx*Sx))

    xMean = Sx / n
    yMean = Sy / n

    print("Sx = ", Sx)
    print("Sy = ", Sy)
    print("Sxy = ", Sxy)
    print("Sxx = ", Sxx)
    print("xMean = ", xMean)
    print("yMean = ", yMean)

    a = yMean - b * xMean

    return (a, b)


def specialLinearRegression(X, Y):
    n = X.shape[0]

    Sxy = 0
    Sxx = 0

    for i in range(n):
        Sxx += (X[i]*X[i])
        Sxy += (X[i]*Y[i])

    a = Sxy / Sxx

    print("Sxy = ", Sxy)
    print("Sxx = ", Sxx)

    return a


x = [4, 5, 7, 8, 9, 10]
y = [5800, 5700, 4200, 4100, 3100, 2500]

X = np.array(x)


Y = np.array(y)


ans = linearRegression(X, Y)

print(ans[0], ans[1])

"""
5

0.698132
0.959931
1.134464
1.570796
1.919862


0.188224
0.209138
0.230052
0.250965
0.313707

"""
