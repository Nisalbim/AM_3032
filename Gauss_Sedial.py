import numpy as np
from numpy.linalg import eig

ep = 10**-3
N = 5
A = np.array([[5,-2,3],[-3,9,1],[2,-1,-7]])
b = np.array([[-1],[2],[3]])

D = np.diag(np.diag(A))
L = np.tril(A,-1) * (-1)
U = np.triu(A,1) * (-1)

inv = np.subtract(D,L)

try:
    g = np.linalg.inv(inv)
except:
    print("Singular Matrix, Inverse not possible.")
T = np.matmul(g,U)
c = np.matmul(g,b)

x_0 = 0
y_0 = 0
z_0 = 0

X_0 = np.array([[x_0],[y_0],[z_0]])

k = 1

while k <= N:
    P= np.matmul(T,X_0)
    X_i = np.add(P,c)
    error_met = np.subtract(X_i,X_0)
    print(X_i)
    print(error_met[(0,0)])
    if (error_met[(0,0)] <= ep) and (error_met[(1,0)] <= ep) and (error_met[(2,0)] <= ep) :
        break
    k = k+1
    X_0 = X_i
print(X_i)
