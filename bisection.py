import numpy as np
import sympy as sym
import matplotlib.pyplot as plt


def f(x):
    return x**3-x-1


def g(p, q):
    if f(p) == 0:
        print("Root is", p)
    elif f(q) == 0:
        print("Root is", q)


def h(r,s):
    g(r, s)
    global a
    a = r
    global b
    b = s
    global c
    c = (r+s)/2


a = 1
b = 2
c = (a+b)/2
error = 10**(-5)
N = 50

if f(a)*f(b) > 0:
    print("There is no root between", a, "and",b)
elif f(a)*f(b) == 0:
    g(a,b)
elif f(a)*f(b) < 0:
    for i in range(0,N):
        if abs(f(c)) >= error:
            if f(c)*f(a) <= 0:
                h(a,c)
            elif f(c)*f(b) <= 0:
                h(c,b)
c = np.around(c,8)
print("Root is of the given equation with 10^-6 accuracy",c)