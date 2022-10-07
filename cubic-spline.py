from turtle import title
import numpy as np 
import matplotlib.pyplot as plt 

#Piecewise interpolation by cubic spline 

# S_i(x_i) = S_i+1(x_i) = f_i 

x_obs = np.array([-2, -1, 0, 1, 2])
f_obs = np.array([0, 1/6, 4/6, 1/6, 0])
N_0, N_2, N_4 = 0, 0, 0

plt.plot(x_obs, f_obs, 'bo', title='Cubic Spline')
plt.show() 