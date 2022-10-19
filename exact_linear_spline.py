import numpy as np 
import matplotlib.pyplot as plt 

x = np.array([-2, 0, 2])
f = np.array([0, 4/6, 0])

def exact_linear_spline(x, f):
    x_vals = []
    y_vals = []
    for i in range(len(x)-1):
        temp_x_val = np.linspace(x[i], x[i+1], 100)
        for temp_x in temp_x_val:
            y = f[i+1] + (((f[i+1] - f[i])/(x[i+1]-x[i]))*(temp_x-f[i]))
            x_vals.append(temp_x)
            y_vals.append(y)
    return x_vals, y_vals 
        

x_1, y_1 = exact_linear_spline(x, f)
plt.plot(x_1, y_1, 'r')
plt.plot(x, f, 'bo')
plt.show()