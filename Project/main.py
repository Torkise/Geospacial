import numpy as np 
import matplotlib.pyplot as plt 
import water_levels
import LSM
import math
import pandas as pd 




lakes = water_levels.get_water_ids()

"""
LSM to estimate water level over whole period     
"""

print(lakes)
date, measurement = water_levels.get_lake_measurement(lakes[0])


for x in measurement: 
    if math.isnan(x):
        date.pop(measurement.index(x))
        measurement.remove(x)
date.pop()
measurement.pop()

y = []
first_date = date[0]
for dt in date: 
    y.append(int((dt - first_date).days))
print(y)
monomials = [0, 1, 2]
coeff = LSM.LSM(y, measurement, [0, 1, 2, 3])
x_i = np.linspace(y[0], y[-1], 100)
y_i = []
for x_val in x_i:
    y_val = 0
    for i in range(3):
        y_val += coeff[i]*x_val**monomials[i]
    y_i.append(y_val)

plt.plot(y, measurement, 'ro')
plt.plot(x_i, y_i, 'b')
plt.show()
