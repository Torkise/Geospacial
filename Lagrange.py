import numpy as np
import random
import matplotlib.pyplot as plt 




def generate_random_polynomial(deg):
    return np.random.random(deg+1)

def get_points_from_random_polynomial(intervall, coeffs):
    x = random.sample(intervall, k=len(coeffs))
    print(x)
    y = np.sum(np.array([[c*dx**i for i, c in enumerate(coeffs)] for dx in x]), axis=1)
    print(y)
    return x, y
    

x = np.array([0, 20, 40, 60, 80, 100])
y = np.array([10, 20, 5, 15, 40, 15])



xplt = np.linspace(x[0], x[-1])
yplt = np.array([], float)

for xp in xplt:
    yp = 0
    
    for xi, yi in zip(x, y):
        yp += yi * np.prod((xp - x[x != xi])/(xi - x[x != xi]))
    yplt = np.append(yplt, yp)

print(xplt)
print(yplt)

plt.plot(x, y, 'ro')
plt.plot(xplt, yplt)
plt.show()