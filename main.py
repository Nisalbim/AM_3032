import numpy as np
A = np.array([[1,2,3],[5,6,7],[3,4,9]])
print(A)
B = A[0:2, 0:2]
C = A[(0,1)]
print(C)
print(B)

