import numpy as np
A = np.array([[2,-1,0,0],[-1,2,-1,0],[0,-1,2,-1],[0,0,-1,2]])
b = np.array([[1],[0],[0],[1]])
N = b.shape[0]
L = np.identity(N)
U = np.identity(N)

L[0,0] = A[1,1]
for n in range(1, N):
    L[n,n-1] = A[n,n-1]
    L[n,n] = A[n,n] - (L[n,n-1]*A[n-1,n])/L[n-1,n-1]
    U[n-1,n] = A[n-1,n]/L[n-1,n-1]

z = np.empty([N,1])
z[0,0] = b[0]/L[0,0]
x = np.empty([N,1])
for j in range(1, N):
    z[j,0] = (b[j,0] - L[j,j-1]*z[j-1,0])/L[j,j]

x[N-1,0] = z[N-1,0]
for m in range(N-2, -1,-1):
    x[m,0] = (z[m,0] - U[m,m+1]*x[m+1,0])
print(z)
print(x)

