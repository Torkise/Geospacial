import numpy as np
x_obs = [0.2, 0.9, 1, 2]
y_obs = [1, 2, -1, -4]
k_val = [0, 1, 2]

def sigma(x, k):
    if abs(x-k) > 1:
        return 0 
    else:
        return 1 - abs(x-k)
    
# Find a matrice 
A = np.zeros((len(x_obs), len(k_val)))

for x in range (len(x_obs)):
    for k in range(len(k_val)):
        A[x][k] = sigma(x_obs[x], k_val[k])

N = A.T@A
a_hat = np.linalg.inv(N)@A.T@y_obs

print("A - matrice ####### \n", A, "\n N matrice = A.T dot A ########\n",N, "\n a hat #####\n",a_hat)
    
def f(x, a_hat, k): 
    sum = 0 
    for i in range(len(k)):
        sum = sum + a_hat[i]*sigma(x, i)
    return sum

f_hat = [f(x, a_hat=a_hat, k = k_val) for x in x_obs]

print("f_hat ###############\n", f_hat)

v = np.array([y_obs[i] - f_hat[i] for i in range(len(y_obs))])
print("v  #############\n", v)

var_0 = (v.T@v)/(len(x_obs)-len(k_val))
var_all = [var_0 * np.linalg.inv(N)[i][i] for i in range(len(k_val))]
print(var_0)
print(var_all)