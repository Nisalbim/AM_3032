import numpy as np
from sympy import poly
from sympy.abc import x
import matplotlib.pyplot as plt

X = np.array([0.9,1.3,1.9,2.1,2.6,3.0,3.9,4.4,4.7,5.0,6.0,7.0,8.0,9.2,10.5,11.3,11.6,12.0,12.6,13.0,13.3])
Y = np.array([1.3,1.5,1.85,2.1,2.6,2.7,2.4,2.15,2.05,2.1,2.25,2.3,2.25,1.95,1.4,0.9,0.7,0.6,0.5,0.4,0.25])

#X = np.array([1,2,3])
#Y = np.array([2,3,5])

N = X.shape[0]
a_j = np.copy(Y).reshape((N,1))

H = np.array([])
for i in range(0, N-1):
    H = np.insert(H,i,X[i+1]-X[i])

b = np.array([[0.00]])
for j in range(1, N-1):
    val_j= np.array([(3/H[j])*(Y[j+1]-Y[j])-(3/H[j-1])*(Y[j]-Y[j-1])])
    b = np.vstack([b,val_j])

b = np.vstack([b,0])
#print(N)

A = np.identity(N)
for k in range(1, N-1):
    A[k,k-1] = H[k-1]
    A[k,k] = 2*(H[k-1]+H[k])
    A[k,k+1] = H[k]
# print(A)

L = np.identity(N)
U = np.identity(N)

L[0,0] = A[1,1]
for n in range(1, N):
    L[n,n-1] = A[n,n-1]
    L[n,n] = A[n,n] - (L[n,n-1]*A[n-1,n])/L[n-1,n-1]
    U[n-1,n] = A[n-1,n]/L[n-1,n-1]

z = np.empty([N,1])
z[0,0] = b[0]/L[0,0]

for j in range(1, N):
    z[j,0] = (b[j,0] - L[j,j-1]*z[j-1,0])/L[j,j]

x_j = np.empty([N,1])
x_j[N-1,0] = z[N-1,0]
for m in range(N-2, -1,-1):
    x_j[m,0] = (z[m,0] - U[m,m+1]*x_j[m+1,0])

b_j = np.empty([N-1,1])
d_j = np.empty([N-1,1])
for i in range(0,N-1):
    b_j[i,0] = ((a_j[i+1,0]-a_j[i,0])/H[i]) - ((x_j[i+1,0]+2*x_j[i,0])/3)*H[i]
    d_j[i,0] = (x_j[i+1] - x_j[i])/3*H[i]

a_j = np.delete(a_j,N-1,axis=0)
c_j = np.delete(x_j,N-1,axis=0)

for i in range(0,4):
    print()
print(a_j)
print(b_j)
print(c_j)
print(d_j)
