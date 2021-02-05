# OM NAMO NARAYANA
import numpy as np
import cmath
import subprocess
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


try:
    from tabulate import tabulate
except:
    install("tabulate")
    from tabulate import tabulate


"""
    complex matrix multiplication for 2D matrix
    if input is in radians the output will be in radians
    if input is in polar form the output will be in polar form


    sample program for ((A*)^T)B
"""

# if the input is in radians, set to true.
radians = False
# if input is in polar form
polar_form = True

# matrix
A = [[(0.15, 0), (0.85, -45)], [(0.85, 45), (0.2, 0)]]
B = [[(0.15, 0), (0.85, -45)], [(0.85, 45), (0.2, 0)]]


def rect_util(_a):
    if radians:
        return cmath.rect(_a[0], _a[1])
    else:
        return cmath.rect(_a[0], _a[1] / 180 * cmath.pi)


def polar_util(_a):
    if radians:
        return cmath.polar(_a)
    else:
        return (cmath.polar(_a)[0], cmath.polar(_a)[1] * 180 / cmath.pi)


def print_rect_util(_a):
    return (_a[0], _a[1])


def rect(row):
    return list(map(rect_util, row))


def polar(row):
    return list(map(polar_util, row))


def print_rect(row):
    return list(map(print_rect_util, row))


if polar_form:
    A = list(map(rect, A))
    B = list(map(rect, B))


"""processing in rectangular form since numpy supports it
    some numpy opreations:
    np.matmul(A, B) returns A@B normal matrix multiplication

    np.dot(A, B) returns dot product of A and B if A and B are one-dimensional vectors.
    !!!Don't use np.dot() for 2d matrix

    np.conj(A) returns conj of matrix A

    np.transpose(A) returns tranpose of matrix A


    some cmath operation
    z = a*exp(jb)
    cmath.rect(a, b) returns rectangular form of z
    z = a + jb
    cmath.polar(a, b) returns polar form of z
    z = 'a+jb'
    cmath.polar(z) returns a+jb
"""

res = np.matmul(np.transpose(np.conj(A)), B)


"""output"""

if polar_form:
    print("polar form")
    if radians:
        print("radians")
    else:
        print("degree")
    res = list(map(polar, res))
else:
    print("rectangular form")
    res = list(map(print_rect, res))

print(tabulate(res, tablefmt="fancy_grid"))
