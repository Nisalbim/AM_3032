import numpy as np

A = np.array([[5,-2,3],[-3,9,1],[2,-1,-7]],dtype=float)
B = np.array([[-1],[2],[3]],dtype=float)

N = 25
error = 10**(-4)
x_0 = np.array([[0],[0],[0]])

U = -1*np.triu(A,1)
L = -1*np.tril(A,-1)
D = np.diag(np.diag(A))

try:
    inv_D = np.linalg.inv(D)
except:
    print("There is a problem")

print(inv_D)

T = np.matmul(inv_D,np.add(L,U))
c = np.matmul(inv_D,B)
x_i = x_0

for k in range(0,N):
    x_n = np.add(np.matmul(T,x_i),c)
    if all((abs(x_n-x_i))<=error):
        print(x_n)
        break
    x_i = x_n
    k = k+1


