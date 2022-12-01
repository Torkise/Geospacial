import numpy as np 
import matplotlib.pyplot as plt 
import math




def a_n(N, L, l, y):
    if N%2 == 0 and l == L:
        # N is Even 
        return (1/(2*N))*sum([y[k]*((-1)**k)*math.cos(2*math.pi*l*(k/N)) for k in range(N)])
    # N is Odd
    else: 
        return (1/N)*sum([y[k]*math.cos(2*math.pi*l*(k/N)) for k in range(N)])

def b_n(N, L, l, y):
    if (N%2 == 0 and l == L): return 0
    return (1/N)*sum([y[k]*math.sin(2*math.pi*l*(k/N)) for k in range(N)])       

def get_y_val(x, f):
    sum_led = 0
    for i in range(1, len(f)):
        if i % 2 == 0:
            sum_led = sum_led + f[i]*math.sin(2*math.pi*x*i/2)
        else:
            sum_led = sum_led + f[i]*math.cos(2*math.pi*x*(i+1)/2)
    return f[0] + 2*sum_led

def B(f, i):
    if i == 0:
        return math.sqrt(f[0]**2)
    if i == 1:
        return math.sqrt(f[1]**2 + f[2]**2)
    

def DTF(y):
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
    
        
        
     


def __init__(y): 
    f = DTF(y)
    print(B(f, 0))
    print(B(f, 1))


y = [1, 3, -1]
__init__(y)

