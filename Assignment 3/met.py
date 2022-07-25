import numpy as np
import sympy as sym

x,y,z = sym.symbols('x,y,z')

A= np.array([[-5,-2,3],[-3,9,1],[2,-1,-7]])\

empt = np.empty(2)
print(empt)
id_met = np.identity(4)
print(id_met)
zer = np.zeros((3,3))
print(zer)
ones = np.ones((3,3))
print(ones)
print(np.diag(A))
print(np.diag(np.diag(A)))

print(A+ones)
print(A-ones)

print(np.matmul(A,ones))

Q = A.transpose()
print(Q)

R = np.linalg.inv(A)
print(np.matmul(A,R))

print(np.triu(A,1))
print(np.tril(A,-1))

A[0,2]=10
print(A)

X = np.array([[x],[y],[z]])
E = np.matmul(A,X)
print(E)

