import numpy as np 

def LSM(x_obs, y_obs, monomials): 
    print("############## \n LSM")
    A = np.array([[x**i for x in x_obs] for i in monomials]).T
    print("A = \n",A)
    N = A.T@A
    print("N = \n", N)
    print("x_hat =  N^-1 * (A.T * y)") 
    x_hat = np.linalg.inv(N)@(np.dot(A.T, y_obs))
    print("coeff: \n", x_hat)
    return x_hat