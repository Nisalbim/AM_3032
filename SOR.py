import numpy as np
from numpy.linalg import eig

# initial conditions given
ep = 10**-4
N = 10
omg = 1.25
A = np.array([[4,3,0],[3,4,-1],[0,-1,4]])
b = np.array([[24],[30],[-24]])
X_0 = np.array([[0],[0],[0]])  # initial guess matrix

if all(np.diag(A)) != 0:  # To use Jacobi method matrix A diagonal elements has to be not equal to zero.
    D = np.diag(np.diag(A))  # diagonal matrix
    L = np.tril(A,-1) * (-1)  # lower triangular matrix
    U = np.triu(A,1) * (-1)   # upper triangular matrix

    P = np.subtract(D,omg*L)  # (D-wL) matrix

    # try to stop if any exception occurred calculating inverse
    try:
        g = np.linalg.inv(P)  # (D-wL)^-1 matrix
    except:
        print("Singular Matrix, Inverse not possible.")

    M = np.add((1-omg)*D,omg*U)  # (1-wL)D+wU matrix
    T = np.matmul(g, M)          # ((D-wL)^-1)*((1-wL)D+wU) matrix
    c = np.matmul(omg*g, b)      # w((D-wL)^-1*b) matrix

    u,v = eig(T)        # spectrum
    m = max(abs(u))     # spectral radius

    k = 1  # number of iterations
    if m < 1:  # To use SOR  method matrix T spectral radius has to be strictly lower than 1.
        print("n", "       ", "x", "       ", "y", "      ", "z")
        print(0, "       ", X_0[0, 0], "       ", X_0[1, 0], "      ", X_0[2, 0])
        while k <= N:
            X_i = np.add(np.matmul(T,X_0) ,c)
            print(k, "       ", X_i[0, 0], "       ", X_i[1, 0], "      ", X_i[2, 0])
            error_met = np.subtract(X_i, X_0)  # error calculate |X_i - X_0|
            if all(abs(error_met) <= ep):  # check all value less than ep value
                print("According to the given tolerance  and number of iterations, the final solution is:")
                print("x =", round(X_i[(0, 0)], 2))
                print("y =", round(X_i[(1, 0)], 2))
                print("z =", round(X_i[(2, 0)], 2))
                break
            X_0 = X_i
            k=k+1
    else:
        print("p((D-wL)^-1)*((1-wL)D+wU)  =",m)
        print("Since ((D-wL)^-1)*((1-wL)D+wU)>1, the given linear system diverges(does not have unique solution).\n Therefore problem can not solve using SOR method")

else:
    print("Coefficient matrix of the given linear system has zero as a diagonal element.")
