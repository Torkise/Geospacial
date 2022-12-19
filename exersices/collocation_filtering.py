import numpy as np 
import math 


# Endre denne til eksponentsiell eller Normal 
exponentiell = True
k = 1 if exponentiell else 2
c = lambda t: 10*math.exp(-0.2*t**k)
var = 0.8
y_t = [1.3, 0.9, 2.3, -3.0]
t_n = [1, 2, 5, 7]

#Gjeldene siffer 
round = 1


# Creates the Co var matrix
c_t_t = np.zeros([len(t_n), len(t_n)])

for i in range(len(c_t_t)):
    for j in range(len(c_t_t[i])): 
        c_t_t[i][j] = c(abs(t_n[j]-t_n[i]))
print("C_t_t \n ######## \n",c_t_t)



c_v_v = c_t_t + var*np.eye(4)
print("C_v_v = \n ######## \n", c_v_v)

y_hat = c_t_t@np.linalg.inv(c_v_v)@y_t 
print("y_hat = \n ##### \n", y_hat)