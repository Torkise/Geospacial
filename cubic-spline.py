from cProfile import label
import numpy as np 
import matplotlib.pyplot as plt 

#Piecewise interpolation by cubic spline 

# S_i(x_i) = S_i+1(x_i) = f_i 

x_obs = np.array([1,20,42,54,60,62,64,87,96,100])
f_obs = np.array([5.159198919210168,-17.828231598350925,-28.161473137025315,-17.010879987552936,-21.488124721662484,-23.909677936121913,-25.669952221088145,-11.659677936121913,-4.454159242573082,5.000000000000012])
x_obs_eq = np.array([1,12,23,34,45,56,67,78,89,100])
f_obs_eq = np.array([5.159198919210168,-10.909677936121913,-15.489848330376985,-18.499705755367124,-26.578231598350920,-17.461494799270707,-25.911473137025315,-9.550358588092315,-12.419952221088138,5.000000000000012])



#Choose f and x 
x = x_obs
f = f_obs
h = np.diff(x)
N_ini = 0
N_fin = 0
n_obs = len(x_obs)
# b 

# TODO : Fikse A 1 vektoren. Den er sykt wack din fitte. Learn to code bitch 
A_1 = np.diag([2*(h[i] + h[i+1]) for i in range(len(h)-1)], 0)
# c 
A_2 = np.diag(h[:-1], 1)
# a 
A_3 = np.diag(h[1:], -1)


A = A_1 + A_2 + A_3 

# Get D vector  ---> What is the d vector? 8 * 1   (n-2), evt (no_spline -1) 
d = [(3*((f[i+1]-f[i])/h[i])* h[i-1]) + (3*((f[i]-f[i-1])/h[i-1])* h[i]) for i in range(1, len(f)-1)]
# N_0 og N_last er null 
# y = d 
y = d

#finn y(1)
#finn y(end)
# N = a/y
N = A / y.T
print(N)


plt.plot(x_obs, f_obs, 'bo', label= 'cubic-spline')
plt.plot(x_obs_eq, f_obs_eq, "r+")
# plt.show() 