import sympy as sym #import sympy lib to do differentiations

x = sym.symbols('x') #variable define
f = x**(1/3)    #function f define
derv = sym.diff(f,x) #differentiate the function

def f(x):
    return x**(1/3)

#defining the given conditions
x_0 = 5
ep = 10 ** -4
N=50

#initial step carried out
x_n = x_0
error = f(x_n)

i = 1
k = 0

#newton raphson method steps
while abs(error) >= ep:
    val = derv.subs(x, x_n) #derivative calculate
    if(val==0):
        print("Derivative become zero")
        k=2
        break
    x_i = x_n - f(x_n)/val  #x_n+1 calculate
    error = abs(f(x_i))     #error value |g(x)|
    print(i, '   ', x_i, '   ', error)
    if i > N:               #if precision not satisfying end the loop finite steps
        print('for 50 iteration no precision satisfying value')
        k = 1
        break
    x_n = x_i               #x values updating
    i = i+1

if (k != 1)&(k != 2):                  #print the root
    print("root of the equation",x_n)