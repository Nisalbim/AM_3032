import numpy as np

X = np.array([0.00,1.34,5.00,10.00,10.60,10.70,10.80,11.40,19.60,20.20,20.30,20.40,21.00,26.00,29.66,31.00])
Y = np.array([0,5,8.66,10,10.4,12,30.2,30.6,30.6,30.2,28.6,10.4,10,8.66,5,0])

a_j = np.copy(X)

N = X.shape[0]
H = np.array([])
for i in range(0, N-1):
    H = np.insert(H,i,X[i+1]-X[i])

print(H[14])
b = np.array([[0.00]])
for j in range(1, N-1):
    val_j= np.array([(3/H[j])*(Y[j+1]-Y[j])-(3/H[j-1])*(Y[j]-Y[j-1])])
    b = np.vstack([b,val_j])

b = np.vstack([b,0])
#print(N)

diagonal = np.array([1.00])
for k in range(1, N-1):
    val_k = 2*(H[k-1]+H[k])
    diagonal = np.insert(diagonal,k,val_k)

diagonal = np.insert(diagonal,N-1,1)
diagonal = np.diag(diagonal)
print(diagonal)



