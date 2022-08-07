import numpy as np
from sympy import poly
from sympy.abc import x

N = int(input("Enter the number of x values: "))
X = []
for i in range(0, N):
    a = float(input("Enter value X_"+str(i)+": "))
    X.append(a)

x_val = float(input("Enter the x value, that function value needed to be calculated: "))

sum = 0

def f(j):
    return (1+j)**(1/2)

Y = []
for i in X:
    Y.append(f(i))

for i in range(0, len(X)):
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
print("Interpolation evaluated value at",x_val,": ",sum(x_val))
print("Absolute error at ",x_val,": ",abs(sum(x_val)-f(x_val)))


