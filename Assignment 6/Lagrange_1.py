import numpy as np
from sympy import poly
from sympy.abc import x

x_0 = 2
x_1 = 2.75
x_2 = 4

sum =0

def f(j):
    return 1/j

def L(k,m,n):
    l = 1/((n - k) * (n - m))
    w = poly((x-k)*(x-m))
    return w*l

X = [x_0,x_1,x_2]
Y = []
for i in X:
    Y.append(f(i))

for i in range(0,len(X)):
    M = X.copy()
    M.pop(i)
    z = L(M[0],M[1],X[i])*Y[i]
    sum = z+sum

print(sum)

