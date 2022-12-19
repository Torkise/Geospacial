import numpy as np
import math 

# c is covar function 
c = lambda t: 10*math.exp(-0.2*t)
# Varians 
var = 0.8
# Points to estimate 
t_p = [2, 6]
# Observed points 
t_n = [1, 2, 5, 7]


# Creates the Co var matrix
c_t_t = np.zeros([len(t_n), len(t_n)])

for i in range(len(c_t_t)):
    for j in range(len(c_t_t[i])): 
        c_t_t[i][j] = c(abs(t_n[j]-t_n[i]))
# print(c_t_t)
    
# plusser på var*Identitestmatrise
c_t_t = c_t_t + var*np.eye(4)
# print(c_t_t)

for p in t_p:
    c_t_p = np.array([c(abs(p- i)) for i in t_n])
    # print(c_t_p)
    variance_in_point = 10
    print("Prediction variance:", p, " = ", variance_in_point - c_t_p.T@np.linalg.inv(c_t_t)@c_t_p)