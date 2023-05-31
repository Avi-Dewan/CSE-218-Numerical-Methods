import numpy as np
import matplotlib.pyplot as plt


def linearRegression(X, Y):
    n = X.shape[0]

    # print(n)

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


x = [0.000000000000001, 0.01, 0.03, 0.05, 0.07,
     0.09, 0.11, 0.13, 0.15, 0.17, 0.19, 0.21]
y = [1, 1.03, 1.06, 1.38, 2.09, 3.54, 6.41, 12.6, 22.1, 39.05, 65.32, 99.78]


X = np.array(x)
Y = np.array(y)


# Exponential Graph. It can be transformed into linear

Z = np.log(Y)
X = np.log(X)

# print(Z)


ans = linearRegression(X, Z)


# print(ans)

A = np.exp(ans[0])
B = ans[1]

print(A, B)


# print(f"BAC of 0.16 have Relative risk of crashing = {round(ans2, 2)}")


plt.scatter(X, Y, color="m", marker="o")


def f(x):
    return A*(x**B)


xValues = X
yValues = f(xValues)

plt.plot(xValues, yValues,  '--', marker='.')
plt.show()
