import numpy as np 
import matplotlib.pyplot as plt 

x = np.array([-2, 0, 2])
f = np.array([0, 4/6, 0])
"""_summary_

x_1 = np.linspace(-2, 0, 100)
x_2 = np.linspace(0, 2, 100)
y_1 = []
y_2 = []
# Sjekk ut f[1] først i ligningen 
for x_i in x_1: 
    y = f[1] + (((f[1] - f[0])/(x[1]-x[0]))*(x_i-f[0]))
    y_1.append(y)
for x_i in x_2:
    # Sjekk ut f[0] til slutt i ligningen 
    y = f[1] + (((f[2] - f[1])/(x[2]-x[1]))*(x_i-f[0]))
    y_2.append(y)
"""
def exact_linear_spline(x, f):
    x_vals = []
    y_vals = []
    for i in range(len(x)-1):
        temp_x_val = np.linspace(x[i], x[i+1], 100)
        for temp_x in temp_x_val:
            y = f[i+1] + (((f[i+1] - f[i])/(x[i+1]-x[i]))*(temp_x-f[0]))
            x_vals.append(temp_x)
            y_vals.append(y)
    return x_vals, y_vals 
        

x_1, y_1 = exact_linear_spline(x, f)
plt.plot(x_1, y_1, 'r')
plt.plot(x, f, 'bo')
plt.show()