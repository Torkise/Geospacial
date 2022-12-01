import numpy as np 
import math

t_i = np.array([0, 2, 4, 6, 8])
ecf = np.array([12.14, 4.33, 0.42, 0.01, 0.001])
exponential = False
start_index = 1
end_index = 2


mat = np.array([[t_i[j] ** i for i in range(end_index)] for j in range(start_index, end_index+1)]).T
# Calculation a hat 
a_hat = np.array(ecf[start_index:end_index+1])@np.linalg.inv(mat)
A_var_est = a_hat[0]
print("a_hat=\n", a_hat)
print("A est : ", A_var_est)
alfa = -(math.log((ecf[start_index]/A_var_est)))/4
print("alfa = ", alfa)

variance = ecf[0] - A_var_est
print(variance)

#Correlation Length
l = math.log(2)/alfa
print(l)