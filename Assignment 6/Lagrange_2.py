import numpy as np
import math
import sympy as sym

from sympy import poly
from sympy.abc import x

x_0 = 0
x_1 = 0.6
x_2 = 4

sum = 0

def fg(j):
    return 1/j

X = [x_0,x_1,x_2]

x = sym.symbols('x')
f = 1/x
mul_er =1
for i in range(0,len(X)):
    f = sym.diff(f,x)
    mul_er = mul_er * poly(x - X[i])

val = abs(f.subs(x, 2))
der = sym.diff(mul_er,x)
root = sym.roots(der)
f_val = []
for i in root:
    if((i>=x_0)&(i<=x_2)):
        f_val.append(abs(mul_er(i)))

g = max(f_val)
error = (val*g)/math.factorial(len(X))

Y = []
for i in X:
    Y.append(fg(i))

for i in range(0,len(X)):
    M = X.copy()
    M.pop(i)
    mul = 1
    den = 1
    for j in range(0,len(M)):
        mul = mul*poly(x-M[j])
        den = den*(X[i]-M[j])
    smul = mul*Y[i]*(1/den)
    sum = smul+sum

print(sum)
#print("Error is:",error)



