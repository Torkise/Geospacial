import numpy as np 
import matplotlib.pyplot as plt 
import math




def a_n(N, L, l, y):
    coeff = (1/2*N) if (N%2 == 0) else (1/N) 
    return (coeff)*sum([y[k]*math.cos(2*math.pi*l*(k/N)) for k in range(N)])

def b_n(N, L, l, y):
    if (N%2 == 0): return 0
    return (1/N)*sum([y[k]*math.sin(2*math.pi*l*(k/N)) for k in range(N)])       


def get_y_val(x, f):
    sum_led = 0
    for i in range(1, len(f)):
        if i % 2 == 0:
            sum_led = sum_led + f[i]*math.sin(2*math.pi*x*i/2)
        else:
            sum_led = sum_led + f[i]*math.cos(2*math.pi*x*(i+1)/2)
    return f[0] + 2*sum_led
            

def DTF(x, y):
    N = len(y)
    L = math.floor(N/2)
    a_0 = (1/N)*sum(y)
    f = [a_0]
    for l in range(1, L+1):
        f.append(a_n(N, L, l, y))
        f.append(b_n(N, L, l, y))
    print("f \n", f)
    
    x = np.linspace(-1, 1, 1001)
    y = [get_y_val(x_i, f) for x_i in x]
    plt.plot(x, y)
    plt.show()
    return f
    
        
        
     


def __init__(x, y): 
    f = DTF(x, y)


x = [0, 1, 2]
y = [1.4, 0.35, -4]
__init__(x, y)

def lol(a):
    return -3/4 + 2*(1.075*math.cos(2*math.pi*a)+1.25*math.sin(2*math.pi*a))

b = np.linspace(-1, 1, 1001)
c = [lol(b_val) for b_val in b]
""""
plt.plot(b, c)
plt.show()
"""