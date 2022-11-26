import numpy as np 
import matplotlib.pyplot as plt 
import math


def a_n(N, L, l, y):
    coeff = (1/2*N) if (N%2 == 0) else (1/N) 
    return (coeff)*sum([y[k]*math.cos(2*math.pi*l*(k/N)) for k in range(N)])

def b_n(N, L, l, y):
    if (N%2 == 0): return 0
    return (1/N)*sum([y[k]*math.sin(2*math.pi*l*(k/N)) for k in range(N)])       

def get_y_val(a_0, x, N, L):
    sum_ledd = sum([a_n(N, L, l, y)*math.cos(2*math.pi*l*x) + b_n(N, L, l, y)*math.sin(2*math.pi*l*x)for l in range(1, L)])
    return a_0 + 2*sum_ledd

def DTF(x, y):
    N = len(x)
    L = math.floor(N/2)
    a_0 = (1/N)*sum(y)
    f = [a_0]
    for l in range(1, L+1):
        f.append(a_n(N, L, l, y))
        f.append(b_n(N, L, l, y))
    print("f \n", f)
    x = np.linspace(x[0], x[-1], 100)
    y = [get_y_val(a_0, x_val, N, L) for x_val in x]
    return x, y
    
        
        
     


def __init__(x, y): 
    x_hat, y_hat = DTF(x, y)
    plt.plot(x, y, 'o',label = 'obs')
    plt.plot(x_hat, y_hat, 'b', label = 'DFT')
    plt.legend()
    plt.show()


x = [-2, 0, 2]
y = [1, 3, -1]
__init__(x, y)