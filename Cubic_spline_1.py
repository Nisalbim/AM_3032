import numpy as np

# X = np.array([0,1.34,5,10,10.6,10.7,10.7,10.8,11.4,19.6,20.2,20.3,20.3,20.4,21,26,29.66,31.00])
# Y = np.array([0,5,8.66,10,10.4,12,28.6,30.2,30.6,30.6,30.2,28.6,12,10.4,10,8.66,5,0])

X = [0,1.34,5,10,10.6,10.7,10.7,10.8,11.4,19.6,20.2,20.3,20.3,20.4,21,26,29.66,31.00]
Y = [0,5,8.66,10,10.4,12,28.6,30.2,30.6,30.6,30.2,28.6,12,10.4,10,8.66,5,0]

H = []
for i in range(0,len(X)-1):
    H.append(X[i+1]-X[i])

np_X = np.array(X)
np_y = np.array(y)

a_j = X.copy()

b =


