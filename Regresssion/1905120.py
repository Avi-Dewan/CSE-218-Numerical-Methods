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


x = [4, 5, 7, 8, 9, 10]
y = [5800, 5700, 4200, 4100, 3100, 2500]


X = np.array(x)
Y = np.array(y)


plt.scatter(X, Y, color="m", marker="o")
plt.show()


# Exponential Graph. It can be transformed into linear

Z = np.log(Y)


# print(Z)


ans = linearRegression(X, Z)


# print(ans)

A = np.exp(ans[0])
B = ans[1]

print(A, B)


ans2 = A*(np.exp(B*0.16))


print(f"BAC of 0.16 have Relative risk of crashing = {round(ans2, 2)}")


# plt.scatter(X, Y, color="m", marker="o")


def f(x):
    return 0.5830482928470333*np.exp(23.817576640308886 * x)


# xValues = X
# yValues = f(xValues)

# plt.plot(xValues, yValues,  '--', marker='.')
# plt.show()
