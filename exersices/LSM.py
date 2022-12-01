import numpy as np 
import matplotlib.pyplot as plt 
import GramSmith

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

def LSM_gram_smith(x_obs, f_obs, monomials): 
    print("################ \n Gram SMith LSM")
    A = np.array([[x**i for x in x_obs] for i in monomials]).T
    P = GramSmith.gram_smith(A)
    S = GramSmith.Gram_Smith_PS(P, A)
    D = []
    for i in P.T: 
        d = (i@f_obs)/(i@i)
        D.append(d)
    D = np.array(D)
    c = D@np.linalg.inv(S.T)
    print("A \n", A)
    print("P \n", P)
    print("S \n", S)
    print("D \n", D)
    print("Coeff \n", c)
    return c
#Run Scripts 
#Define Variables 
x_obs = [0, 1, 2, 3, 4, 5]
f_obs = [5/6, 4/6,2/6, 0, 1/6, 0]
monomials = [0, 1]
coeff = LSM_gram_smith(x_obs, f_obs, monomials)
x = np.linspace(x_obs[0], x_obs[-1], 1000)
y = []
for x_val in x:
    y_val = 0
    for i in range(len(monomials)):
        y_val += coeff[i]*x_val**monomials[i]
    y.append(y_val)
#Plot
plt.plot(x_obs, f_obs, 'bo', label = 'Observed Points')
plt.plot(x, y, 'g', label = 'LSM estimate')
plt.title('LSM')
plt.legend()
plt.show()


    