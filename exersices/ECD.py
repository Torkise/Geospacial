import numpy as np 
import math

t_i = np.array([0, 2, 4, 6, 8])
ecf = np.array([12.14, 4.33, 0.42, 0.01, 0.001])
# False if Normal, True if exponential 
exponential = True
# Fill in the efc to solve the Least Square
første_punkt = 1
siste_punkt = 3
rounding = 2
t_i_lsm = np.array(t_i[første_punkt:siste_punkt+1])
efc_lsm = np.array(ecf[første_punkt:siste_punkt+1])

# Denne skal være transponert for å gi riktige verdier ifølge LF. Sjekk med Freddie 

efc_c = np.array([[i**0, i**1, i**2] for i in t_i_lsm]).T

# Calculation a_hat using LSM 
a_hat = efc_lsm@np.linalg.inv(efc_c)
for i in range(len(a_hat)):
    a_hat[i] = round(a_hat[i], rounding)
A_var_est = a_hat[0]


print("a_hat=\n", a_hat)
print("A est : a_hat[0] = ", A_var_est)

# Husk å sette exponetsiell til True / False 
k = 1 if exponential else 2
alfa = -(math.log((efc_lsm[0]/A_var_est)))/t_i_lsm[0]**k
alfa = round(alfa, rounding)
print("alfa = ", alfa)

variance = ecf[0] - A_var_est
variance = round(variance, rounding)
print("Variance = A - efc(0): ", variance)

# Sett opp Linearisering! 

#Correlation Length    efc(tau) = 1/2 ecf(0)
l = math.log(2)/alfa if exponential else math.sqrt(math.log(2)/alfa) 
l = round(l, rounding)
print("correlation length\n",l)
