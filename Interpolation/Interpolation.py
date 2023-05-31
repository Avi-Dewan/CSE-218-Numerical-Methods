import numpy as np
import matplotlib.pyplot as plt

# 13	7.9
# 16	6.7
# 20	5.5
# 24	4.3


def product(i, value, x):
    r = 1
    for j in range(i):
        r = r*(value - x[j])

    return r


def dividedDiff(x, y, n):

    for i in range(1, n):
        for j in range(n-i):
            y[j][i] = ((y[j][i-1] - y[j+1][i-1]) / (x[j] - x[i+j]))

    return y


def interpolation(val, x, y, n):

    y = dividedDiff(x, y, n)

    s = y[0][0]

    for i in range(1,  n):
        s = s + (product(i, val, x)*y[0][i])

    return s


x = [13, 16, 20, 24]
y = [[0 for i in range(10)] for j in range(10)]

y[0][0] = 7.9
y[1][0] = 6.7
y[2][0] = 5.5
y[3][0] = 4.3

value = int(input("Enter the time: "))

ans = interpolation(value, x, y, 4)

print(ans)


"""
xValues = np.arrange(1, 30)
yValues = []

for i in range(1, 30):
    yValues.append(interpolation(i, x, y, 4))

plt.plot(xValues, yValues, '--', marker='.')
plt.title("Graph for finding two points of Bisection")
plt.xlabel("x (m)")
plt.ylabel("f(x)")
plt.show()
"""
