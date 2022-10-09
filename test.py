import numpy as np
import matplotlib.pyplot as plt 

x = [-2, 0, 2]
f = [0, 4/6, 0]
plt.plot(x, f, 'r+')

x = np.linspace(-2, 2, 100)
f = []
for x_val in x:
    f.append(1/3)

plt.plot(x, f, 'b')
plt.show()