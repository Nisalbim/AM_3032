import numpy as np #import numpy lib

#defining the f function
def f(x):
    return x**3 + 4*x**2-10

#defining the g function
def g(x):
    return ((10/x+4))**0.5

#defining the given conditions
x_0 = 1.5
ep = 10 ** -5

# inital step was carried out
x_n = x_0
x_i = g(x_0)
print(1, '   ', x_n, '   ', x_i, '   ', abs(x_n - x_i)) #print that step

i = 1
k = 0

#fixed point iterations
while abs(x_n - x_i) >= ep:
    x_n = x_i    #x value
    x_i = g(x_n) #g(x) value
    print(i+1, '   ', x_n, '   ', x_i, '   ', abs(x_n - x_i)) #print that step
    if i > 50:  #if precision not satisfying end the loop finite steps
        print('for 50 iteration no precision satisfying value')
        k = 1
        break
    i = i+1

if k != 1: #print the root
    print("root of the equation", x_i)


