import numpy as np #import numpy library
def f(x):          #function defining
    return x**3 - x -1
a=1
b=2
error =10**(-5)

if f(a)*f(b)>0:   #identify root exist or not
    print("Bisection method fails")

if f(a)*f(b)==0:  #identify root isn the end of given interval
    if f(a)==0:
        print("print root is:", a)
    else:
        print("print root is:", b)

a_n=a             #assigning to new variables
b_n=b
print("Initial interval is:[",a_n,",",b_n,"]")
k=0

while abs(f(b_n))>=error or abs(f(a_n))>=error:   #stopping criteria.To both end points function value less than epsilon
    sub_int = np.linspace(a_n,b_n,21)     #dividingthe interval into 20 sub intervals iteration by iteration
    k=k+1
    print("Iteration",k,"subintervals are:",sub_int)
    for i in range(len(sub_int)):
        if f(sub_int[i])*f(sub_int[i+1])<0: #identify root is in between the end of the given interval
            a_n = sub_int[i]
            b_n = sub_int[i+1]
            break
        elif f(sub_int[i])*f(sub_int[i+1])==0:  #identify root is at the end of the given interval
            if f(sub_int[i])==0:
                print("print root is:", f(sub_int[i]))
            else:
                print("print root is:", f(sub_int[i+1]))
            break
    print("Iteration",k,"interval is:","[",a_n,",",b_n,"]")



