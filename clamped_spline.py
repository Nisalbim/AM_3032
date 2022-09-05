import numpy as np
import math
import matplotlib.pyplot as plt
from sympy import poly
from sympy.abc import x

# X = np.array([[1],[2],[3]])
# Y = np.array([[2],[3],[5]])
X = np.array([[0],[1],[2],[3]])
Y = np.array([[1],[math.exp(1)],[math.exp(2)],[math.exp(3)]])
FPO = 1
FPN = math.exp(3)
N = X.shape[0]

a_j = np.copy(Y)
a_j = np.delete(a_j,N-1,0)

H = np.zeros((N-1,1))
for i in range(0,N-1):
    H[i,0] = X[i+1,0]-X[i,0]

b = np.zeros((N,1))
alpha_0 = (3*(Y[1,0]-Y[0,0]))/(H[0,0])-3*FPO
alpha_n = 3*FPN - 3*(Y[N-1,0]-Y[N-2,0])*(1/H[N-2,0])
b[0,0] = alpha_0
b[N-1,0] = alpha_n
print(alpha_0,alpha_n)
for i in range(1,N-1):
    b[i,0] = ((3/H[i,0])*(Y[i+1,0]-Y[i,0]))-((3/H[i-1,0])*(Y[i,0]-Y[i-1,0]))

L = np.zeros((N,1))
U = np.zeros((N,1))
z = np.zeros((N,1))

L[0,0] = 2*H[0,0]
U[0,0] = 0.5
z[0,0] = alpha_0/L[0,0]

for i in range(1,N-1):
    L[i,0] = (2*(X[i+1,0]-X[i-1,0]))-(H[i-1,0]*U[i-1,0])
    U[i,0] = H[i,0]/L[i,0]
    z[i,0] = (b[i,0]-(H[i-1,0]*z[i-1,0]))/L[i,0]
print(L)

L[N-1,0] = H[N-2,0]*(2-U[N-2,0])
z[N-1,0] = (alpha_n - (H[N-2,0]*z[N-2,0]))/L[N-1,0]
c_j = np.copy(z)

b_j = np.zeros((N-1,1))
d_j = np.zeros((N-1,1))
for j in range(N-2,-1,-1):
    c_j[j,0] = z[j,0] - U[j]*c_j[j+1]
    b_j[j,0] = ((Y[j+1,0] - Y[j,0])/H[j,0]) - ((H[j,0]*(c_j[j+1,0]+2*c_j[j,0]))/3)
    d_j[j,0] = ((c_j[j+1,0]-c_j[j,0])/(3*H[j,0]))

c_j = np.delete(c_j,N-1,0)

for i in range(0,N-1):
    s_i = a_j[i,0] + b_j[i,0]*poly(x-X[i,0]) + c_j[i,0]*(poly(x-X[i,0])**2) +d_j[i,0]*(poly(x-X[i,0])**3)
    print(s_i)
    x_val = np.linspace(X[i,0],X[i+1,0],20)
    y_val = np.zeros((20,1))
    for k in range(0,20):
        y_val[k] = s_i(x_val[k])
    plt.plot(x_val,y_val,'b')
X_0 = np.linspace(X[0,0],X[N-1,0],60)
Y_0 = np.exp(X_0)
#plt.plot(X_0,Y_0,'r')
plt.legend(['Approximation','true curve'])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Cubic spline according to clamped')
plt.show()
