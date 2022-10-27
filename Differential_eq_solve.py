import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

def f(r, s):
    return s-r**2+1


def g(r):
    return (r+1)**2-0.5*np.exp(r)


y_0 = 0.5
h = 0.5
t_i = 0

y_i = y_0
t = np.array([t_i])
y = np.array([y_i])

while t_i < 2:
    y_i = y_i + h*f(t_i,y_i)
    y = np.append(y, [y_i])
    t_i = t_i + h
    t = np.append(t, [t_i])
print(t)
print(y)
N = t.shape[0]
z = np.zeros(N)

for i in range(0,N):
    z[i] = g(t[i])
print(z)
plt.plot(t,y,'or')
plt.plot(t,z,'*b')
plt.show()


