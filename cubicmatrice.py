from sympy import poly
from numpy.linalg import eig
import numpy as np
from sympy.abc import x,a,b,c,d,e,f,g,h
from sympy import diff
from itertools import permutations 
def coe(p,l):                           #function to calculate coefficients for each of the variables
    v=poly(p,l)
    list5=v.all_coeffs()
    list5.pop()
    if list5==[]:
        return 0
    else:
        return float(list5[0])
list1=[0,1,2]
list2=[0,1,2]
list3=[1,1]
S0=b*(x-list1[0])+c*(x-list1[0])**2+d*(x-list1[0])**3 #interpolation polynomial of the first half of the interval
S1=f*(x-list1[1])+g*(x-list1[1])**2+h*(x-list1[1])**3 #interpolation polynomial  of the 2nd half of the interval

#derivatives

S0_1=diff(S0,x)   
S0_2=diff(S0_1,x) 
S1_1=diff(S1,x)  
S1_2=diff(S1_1,x)

# calculating equations 
x=list1[0]
r1=eval(str(S0_1))#boundry

x=list1[1]
r3=eval(str(S0))#function value
r2=eval(str(S1_1))-eval(str(S0_1))#equal of 1st derivative
r5=eval(str(S1_2))-eval(str(S0_2))#equal of 2nd derivative

x=list1[2]
r4=eval(str(S1))#function value
r6=eval(str(S1_1))#boundry
rhs_old=[list3[0],0,list2[1]-list2[0],list2[2]-list2[1],0,list3[1]] #right hand side of the equations
print(r1)
print(r2)
print(r3)
print(r4)
print(r5)
print(r6)


list6=[r1,r2,r3,r4,r5,r6]

new_dict = {list6[n]: rhs_old[n] for n in range(len(rhs_old))}
list6_p=list(permutations(list6))
j=0
#while loop to get the correct order of equations for the gauss seidel method
while j <len(list6_p):
    list7= list6_p[j]
    if (coe(list7[0],b)==0 or coe(list7[1],c) == 0 or coe(list7[2],d)==0 or coe(list7[3],f)==0 or coe(list7[4],g)==0 or coe(list7[5],h)==0):#checking for 0s in diagonal
        j+=1
    else:
        list7= list6_p[j]
        rhs=np.array([[new_dict[list7[0]]],[new_dict[list7[1]]],[new_dict[list7[2]]],[new_dict[list7[3]]],[new_dict[list7[4]]],[new_dict[list7[5]]]])#right hand side of the system 
        
        r1=list7[0]
        r2=list7[1]
        r3=list7[2]
        r4=list7[3]
        r5=list7[4]
        r6=list7[5]
        a=np.array([[coe(r1,b),coe(r1,c),coe(r1,d),coe(r1,f),coe(r1,g),coe(r1,h)],     #coefficient matrix
                   [coe(r2,b),coe(r2,c),coe(r2,d),coe(r2,f),coe(r2,g),coe(r2,h)],
                    [coe(r3,b),coe(r3,c),coe(r3,d),coe(r3,f),coe(r3,g),coe(r3,h)],
                    [coe(r4,b),coe(r4,c),coe(r4,d),coe(r4,f),coe(r4,g),coe(r4,h)],
                    [coe(r5,b),coe(r5,c),coe(r5,d),coe(r5,f),coe(r5,g),coe(r5,h)],
                    [coe(r6,b),coe(r6,c),coe(r6,d),coe(r6,f),coe(r6,g),coe(r6,h)]])
        #Gauss-Seidel method
        D=np.diagflat(np.diag(a))  #diagonal matrix
        f1=np.triu(a,1)*-1  #upper triangular matrix
        g1=np.tril(a,-1)*-1  #lower triangular matrix
        h1=np.linalg.inv(D)  #inverse of the diagonal matrix
        G=np.linalg.inv(D-g1) # (D-L)^-1 matrix
        
        
        H=np.dot(G,f1)
        u,v=eig(H)
        m=max(abs(u)) #here m is the spectral radius
        if m<1:
            x_no=np.array([[0],[0],[0],[0],[0],[0]])#initial guess
            y=np.dot(f1,x_no) +rhs
            x_n=np.dot(G,y)
            count=1
            while  any(np.abs((x_n-x_no))> 0.00001):
                x_no=x_n
                y=np.dot(f1,x_no) +rhs
                x_n=np.dot(G,y)
                count+=1
            print("a0=",list2[0])
            print("b0=",x_n[0])
            print("c0=",x_n[1])
            print("d0=",x_n[2])
            
            print("a1=",list2[1])
            print("b1=",x_n[3])
            print("c1=",x_n[4])
            print("d1=",x_n[5])
            print("Hence the polynomials")
            print("S0="+str(list2[0])+"+"+str(x_n[0])+"*(x-"+str(list1[0])+")+"+str(x_n[1])+"*(x-"+str(list1[0])+")**2+"+str(x_n[2])+"*(x-"+str(list1[0])+")**3")
            print("S1="+str(list2[1])+"+"+str(x_n[3])+"*(x-"+str(list1[1])+")+"+str(x_n[4])+"*(x-"+str(list1[1])+")**2+"+str(x_n[5])+"*(x-"+str(list1[1])+")**3")
            
            
            j+=1
        else:
            j+=1
