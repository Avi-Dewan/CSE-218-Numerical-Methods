import numpy as np
import matplotlib.pyplot as plt


def GaussianElimination(A, B, pivot=True, showall=True):
    n = A.shape[0]

    ans = np.zeros(n)

    # forward elimination:
    for i in range(0, n-1):
        # finding max and swapping
        if pivot:
            maxRow = i
            for j in range(i+1, n):
                if np.abs(A[j][i]) > np.abs(A[maxRow][i]):
                    maxRow = j

            if maxRow != i:
                for x in range(0, n):
                    temp = A[i][x]
                    A[i][x] = A[maxRow][x]
                    A[maxRow][x] = temp

                temp2 = B[i]
                B[i] = B[maxRow]
                B[maxRow] = temp2

        for r in range(i+1, n):
            m = A[r][i] / A[i][i]

            for c in range(i, n):
                A[r][c] = A[r][c]*1.0 - m*A[i][c]

            B[r] = B[r] - m*B[i]

            if showall:

                print("A : ")
                print("[ ", end="")
                k = 0
                for r in A:
                    for c in r:
                        print(f'{c:.4f}', end=" ")
                    if k != n-1:
                        print()
                    k += 1
                print("]")

                print("B : ")
                print("[ ", end="")
                for c in B:
                    print(f'{c:.4f}', end=" ")
                print("]\n")

    # Back Substitution

    ans[n-1] = B[n-1]/A[n-1][n-1]

    for i in range(n-2, -1, -1):
        tmp = B[i]
        for l in range(n-1, i, -1):
            tmp -= ans[l]*A[i][l]

        ans[i] = tmp/A[i][i]

    return ans


n = int(input("Enter the number of unknowns: "))


ar = []

for i in range(n):
    r = []
    for j in range(n):
        r.append(float(input()))

    ar.append(r)

A = np.array(ar)


br = []

for i in range(n):
    br.append(float(input()))

B = np.array(br)

print("A = ", A)
print()
print("B = ", B)


print()
print()

ans = GaussianElimination(A, B)

print("Ans----> ")

for a in ans:
    print(f'{a:.4f}')


"""
3
25
5
1
64
8
1
144
12
1
106.8
177.2
279.2
"""

"""
 3
20
15
10
-3
-2.249
7
5
1
3
45
1.751
9
"""

"""
n = int(input("Enter the number of unknowns: "))

input()

A = np.array([input().strip().split() for _ in range(n)], float)

input()

B = np.array([input().strip().split() for _ in range(n)], float)
"""
