import numpy as np
import matplotlib.pyplot as plt

def gradient_descent(x,y):
    m_curr = b_curr = 0
    it = 1000
    if(len(x)==len(y)):
        n = len(x)
        learning_rate = 0.1
        #plt.xlim(0,5)
        #plt.ylim(0,15)
        plt.plot(x,y,color='red',marker='*',linewidth='1')
        for i in range(it):
            y_pred = m_curr * x + b_curr
            plt.plot(x,y_pred,color='green')
            #cost = (1/n)*sum((val**2 for val in (y-y_pred)))
            cost = (1 / n) * sum((y - y_pred)**2)
            md = (2/n)*sum(-x*(y-y_pred))
            bd = (2 / n) * sum(-(y - y_pred))
            m_curr = m_curr - learning_rate * md
            b_curr = b_curr - learning_rate * bd
            #print("m {}, b{}, cost {} iteration {}".format(m_curr,b_curr, cost,i))
        plt.show()
    else:
        print("Enter equal length arrays")


x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

gradient_descent(x,y)