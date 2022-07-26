# import numpy library
import numpy as np
from numpy.linalg import eig

# initial conditions given
ep = 10**-4
N = 100
A = np.array([[1,2,-2],[1,1,1],[2,2,1]])
b = np.array([[7],[2],[5]])
x_0 = 0
y_0 = 0
z_0 = 0

if all(np.diag(A)) != 0:  # To use gauss seidal method metrix A diagonal elements has to be not equal to zero.
    D = np.diag(np.diag(A))  # diagonal metrix
    L = np.tril(A,-1) * (-1)  # lower triangular metrix
    U = np.triu(A,1) * (-1)   # upper triangular metrix

    inv = np.subtract(D,L)  # (D-L) metrix

    # try to stop if any exception occurred calculating inverse
    try:
        g = np.linalg.inv(inv)  # (D-L)^-1 metrix
    except:
        print("Singular Matrix, Inverse not possible.")

    T = np.matmul(g,U)  # (D-L)^-1*U
    c = np.matmul(g,b)  # (D-L)^-1*b

    u,v = eig(T)        # spectrum
    m = max(abs(u))     # spectral radius
    print(m)

    X_0 = np.array([[x_0],[y_0],[z_0]])  # initial guess metrix

    k = 1   # number of iterations

    if m < 1:  # To use gauss seidal method metrix T spectral radius has to be strictly lower than 1.
        print("n", "       ", "x", "       ", "y", "      ", "z")
        print(0, "       ", X_0[0, 0], "       ", X_0[1, 0], "      ", X_0[2, 0])

        while k <= N:
            P = np.matmul(T,X_0)    # iterating step
            X_i = np.add(P,c)
            print(k, "       ", X_i[0, 0], "       ", X_i[1, 0], "      ", X_i[2, 0])
            error_met = np.subtract(X_i,X_0)  # error calculate |X_i - X_0|
            if all(abs(error_met) <= ep):   # check all value less than ep value
                print("According to the given tolerance  and number of iterations,\n the final solution rounded up to two digits is:")
                print("x =", round(X_i[(0, 0)],2))
                print("y =", round(X_i[(1, 0)],2))
                print("z =", round(X_i[(2, 0)],2))
                break
            X_0 = X_i
            k = k + 1
    else:
        print("p((D-L)^-1*U) =", m)
        print("Since p((D-L)^-1*U)>1, the given linear system diverges(does not have unique solution).\n Therefore problem can not solve using gauss seidal method")

else:
    print("Coefficient matrix of the given linear system has zero as a diagonal element.")
