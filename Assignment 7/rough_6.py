import numpy as np
import sympy as sym
x = sym.symbols('x')
import matplotlib.pyplot as plt

# input x,f(x) arrays
X = np.array([0.00,1.34,5.00,10.00,10.60,10.70,10.80,11.40,19.60,20.20,20.30,20.40,21.00,26.00,29.66,31.00])
Y = np.array([0.00,5.00,8.66,10.00,10.40,12.00,30.20,30.60,30.60,30.20,12.00,10.40,10.00,8.66,5.00,0.00])


N = X.shape[0]
a_j = np.copy(Y).reshape((N,1))

# h_j values array
H = np.array([])
for i in range(0, N-1):
    H = np.insert(H,i,X[i+1]-X[i])

# building the RHS side of C equation system
b = np.array([[0.00]])
for j in range(1, N-1):
    val_j= np.array([(3/H[j])*(Y[j+1]-Y[j])-(3/H[j-1])*(Y[j]-Y[j-1])])
    b = np.vstack([b,val_j])
b = np.vstack([b,0])

# building the coefficient matrix of C equation system
A = np.identity(N)
for k in range(1, N-1):
    A[k,k-1] = H[k-1]
    A[k,k] = 2*(H[k-1]+H[k])
    A[k,k+1] = H[k]

# building Lower and upper triangular matrices
L = np.identity(N)
U = np.identity(N)

L[0,0] = A[0,0]
for n in range(1, N):
    L[n,n-1] = A[n,n-1]
    L[n,n] = A[n,n] - (L[n,n-1]*A[n-1,n])/L[n-1,n-1]
    U[n-1,n] = A[n-1,n]/L[n-1,n-1]

# solving the system and find z values
z = np.empty([N,1])
z[0,0] = b[0]/L[0,0]

for j in range(1, N):
    z[j,0] = (b[j,0] - L[j,j-1]*z[j-1,0])/L[j,j]

# solving the system and find c values
x_j = np.empty([N,1])
x_j[N-1,0] = z[N-1,0]
for m in range(N-2, -1,-1):
    x_j[m,0] = (z[m,0] - U[m,m+1]*x_j[m+1,0])

# calculate d values and b values
b_j = np.empty([N-1,1])
d_j = np.empty([N-1,1])
for i in range(0,N-1):
    b_j[i,0] = ((a_j[i+1,0]-a_j[i,0])/H[i]) - ((x_j[i+1,0]+2*x_j[i,0])/3)*H[i]
    d_j[i,0] = (x_j[i+1,0] - x_j[i,0])/(3*H[i])

# deleting last element of a_j and c_j arrays
a_j = np.delete(a_j,N-1,axis=0)
c_j = np.delete(x_j,N-1,axis=0)

# Coefficients of splines polynomials
sol = np.copy(a_j)
sol = np.insert(sol,[1],b_j,axis=1)
sol = np.insert(sol,[2],c_j,axis=1)
sol = np.insert(sol,[3],d_j,axis=1)

# printing polynomials
polyn = np.array([])
for i in range(0,N-1):
    t=str(float(a_j[i]))+"+("+str(float(b_j[i]))+")*(x-"+str(X[i])+")+("+str(float(c_j[i]))+")*(x-"+str(X[i])+")**2+("+str(float(d_j[i]))+")*(x-"+str(X[i])+")**3"
    polyn = np.append(polyn,t)
print(polyn)

# plotting splines
for i in range(0,N-1):
    eq = 0
    for j in range(0,4):
        eq = sol[i,j]*((x-X[i])**j) + eq
    x_values = np.linspace(X[i],X[i+1],1000)
    y_values = []
    for i in x_values:
        y_values.append(eq.subs(x, i))
    plt.plot(x_values, y_values, color="blue")

for i in range(0,N-1):
    plt.plot(X[i],Y[i],'ro')

plt.xlabel('x_axis')
plt.ylabel('y_axis')
plt.title("Cubic spline interpolation")
plt.show()

