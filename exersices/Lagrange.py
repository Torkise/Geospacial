from cProfile import label
import numpy as np
import matplotlib.pyplot as plt 

x_obs = np.array([0, 20, 40, 60, 80, 100])
y_obs = np.array([10, 20, 5, 15, 40, 15])

def getAlfa(x):
    return np.array([x**i for i in range(len(x_obs-1))])

# f = np.dot(a. F)
F = np.array([[x**i for x in x_obs] for i in range(len(x_obs)-1)])
f = F@y_obs
#coeffisientene til q. 
print(f)

xplt = np.linspace(x_obs[0], x_obs[-1], 101)
yplt = np.array([], float)

for xp in xplt: 
    yp = 0
    for xi, yi in zip(x_obs, y_obs):
        yp += yi * np.prod((xp - x_obs[x_obs != xi])/(xi - x_obs[x_obs != xi]))
    yplt = np.append(yplt, yp)

plt.plot(x_obs, y_obs,' bo', label = "observations")
plt.plot(xplt, yplt, 'r', label = 'estimate')
plt.legend()
plt.show()