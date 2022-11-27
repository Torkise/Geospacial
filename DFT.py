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
    N = len(y)
    L = math.floor(N/2)
    a_0 = (1/N)*sum(y)
    f = [a_0]
    for l in range(1, L+1):
        f.append(a_n(N, L, l, y))
        f.append(b_n(N, L, l, y))
    print("f \n", f)
    return f
    
        
        
     


def __init__(x, y): 
    f = DTF(x, y)


x = [0, 1, 2]
y = [1.4, 0.35, -4]
__init__(x, y)