from sre_constants import OP_LOCALE_IGNORE
import numpy as np
import matplotlib.pyplot as plt


def newtonRhapson(x, a, max):
    old = x

    err = 100

    print("Iteration --- Root ---- ARAE")

    for i in range(0, max):

        new = old - (f(old)/diffF(old))

        err = np.abs(((new - old) / new)*100)

        print(i+1, "---- ", new, " ----", err)

        if(err < a):
            break

        old = new

    return new


def f(x):
    return ((x**3) - (0.18*x*x) + (0.0004752))


def diffF(x):
    return 3*x*x - 0.36*x


def zero(x):
    return 0*x


xValues = np.arange(0, 0.13, .005)
yValues = f(xValues)
zeroValues = zero(xValues)

plt.plot(xValues, yValues, xValues, zeroValues,  '--', marker='.')
plt.title("Graph for finding initial guess for Newton-Rhapson")
plt.xlabel("x (m)")
plt.ylabel("f(x)")
plt.show()

print("The approximate value of the root is: ", newtonRhapson(0.06, 0.05, 20))

print()
