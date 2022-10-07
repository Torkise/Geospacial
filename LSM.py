import numpy as np 
import matplotlib.pyplot as plt 
f_obs = np.array([5.159198919210168,-6.488124721662475,-16.115977244587206,-12.550358588092320,-17.300358588092320,-12.163010271764966,-12.365977244587214,-11.954838183125013,-6.578231598350914,5.000000000000012])
x_obs = np.array([1,10,15,28,53,88,90,91,95,100])
n_obs = len(x_obs)
n_coeff = 3
F = np.array([np.array(x_obs)**i for i in range(2, -1, -1)]).T
y = f_obs[:,np.newaxis]
coeffs = np.dot(np.linalg.inv(np.dot(F.T, F)), np.dot(F.T, f_obs))
print(coeffs)
plt.scatter(x_obs, f_obs)
x = np.linspace(0, 100)
plt.plot(x, coeffs[0]*x**2 + coeffs[1]*x + coeffs[2])
plt.show()
