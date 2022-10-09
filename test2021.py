from cProfile import label
import numpy as np 
import matplotlib.pyplot as plt 

x = [-1, 0, 2]
f = [1, 2, -1]

plt.plot(x, f, 'o', label='observations')
plt.title("Test")


#Exact linear spline test
x = []
y = []
for x_val in np.linspace(-1, 0, 100):
    x.append(x_val)
    y.append(2 + x_val)
for x_val in np.linspace(0, 2, 200):
    x.append(x_val)
    y.append(2 - x_val/4)

plt.plot(x, y, label = 'linear spline')
x = []
y = []
for x_val in np.linspace(-1, 2, 100):
    x.append(x_val)
    y_val = (1/6)*(-5*x_val**2 + x_val + 12)
    y.append(y_val)
    
plt.plot(x,y, label='lagrange')

#Excat cubic spline

#Show Plot 
plt.legend()
plt.show()

#Lagrange Test 