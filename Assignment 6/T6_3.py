import numpy as np
from sympy import poly
from sympy.abc import x

N = int(input("Enter the number of x values: "))
X = []
Y = []
for i in range(0, N):
    a = float(input("Enter value X_"+str(i)+": "))
    X.append(a)
    b = float(input("Enter value Y_"+str(i)+": "))
    Y.append(b)

x_val = float(input("Enter the x value, that function value needed to be calculated: "))

sum = 0

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



