
def f(x): #function defining
    return x**3 - x -1
a = 1
b = 2

if f(a)*f(b)>0: #identify root exist or not
    print("Bisection method fails")

if f(a)*f(b)==0:  #identify root isn the end of given interval
    if f(a)==0:
        print("print root is:", a)
    else:
        print("print root is:", b)

a_n=a #assigning to new variables
b_n=b
c=(a_n+b_n)/2 #mid point defining
print("Initial interval is:[",a_n,",",b_n,"]")
i = 0

while abs(f(c))>=10**(-5): #stopping criteria
    i=i+1
    if f(a_n)*f(c)<0: #interval updating
        b_n=c
    elif f(b_n)*f(c)<0:  #interval updating
        a_n=c
    elif f(c)==0:
        break
    c=(a_n+b_n)/2
    print("Iteration",i,"interval is:","[",a_n,",",b_n,"]")

print("root is:", c)
