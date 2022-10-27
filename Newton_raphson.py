import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

def f(x):
    return x**4-x-10

x = np.linspace(-3,3,1001,endpoint=True)
y = np.zeros(len(x))

for i in range(0,len(x)):
    y[i] = f(x[i])

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.plot(x,y,'-')
plt.ylim(-12,12)
plt.show()