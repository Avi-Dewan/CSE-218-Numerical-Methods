import numpy as np
import matplotlib.pyplot as plt


def bisection(l, u, a, max):

    old = (l + u) / 2
    err = 100

    for i in range(0, max):

        mid = (l+u) / 2

        if i != 0:
            err = np.abs(((mid - old) / mid)*100)

        if(f(l)*f(mid) < 0):
            u = mid
        elif(f(l)*f(mid) > 0):
            l = mid
        else:
            return mid

        if(err < a):
            return mid

        old = mid

    return mid


def bisectionIterate(l, u, a, max):

    old = (l + u) / 2
    err = 100

    print("Iteration No. --- Mid Value ---    ARAE")
    print()

    for i in range(0, max):

        mid = (l+u) / 2

        print("Iteration ", end="")

        if(i < 9):
            print("0", end="")

        print(i + 1, " --- ", "%.5f" % mid,  end="  --- ")

        if i == 0:
            print("   No ARAE for the first one", end="")
        else:
            err = np.abs(((mid - old) / mid)*100)
            print("  ", err, end="")

        print("____ l =", "%.5f" % f(l), "____ m = ", "%.5f" %
              f(mid), "____ u = ", "%.5f" % f(u))

        if(f(l)*f(mid) < 0):
            u = mid
        elif(f(l)*f(mid) > 0):
            l = mid
        # else:
        #     return mid

        old = mid

    return mid


def f(x):
    return ((x**3) - (0.18*x*x) + (0.0004752))


def zero(x):
    return 0*x


xValues = np.arange(0, 0.13, .005)
yValues = f(xValues)
zeroValues = zero(xValues)

plt.plot(xValues, yValues, xValues, zeroValues,  '--', marker='.')
plt.title("Graph for finding two points of Bisection")
plt.xlabel("x (m)")
plt.ylabel("f(x)")
plt.show()


print("The approximate value of the root is: ", bisection(0, 0.12, 0.5, 20))

print()

bisectionIterate(0, 0.12, 0.5, 20)
