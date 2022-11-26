import numpy as np 
import matplotlib.pyplot as plt 
import math

x_obs = [-1, -1/2, 1, 0.2]
y_obs = [1, 1/2, 1, 0.3]
f_obs = [1, 3, 2, 1]

def weight(d):
    if d <= 1:
        return (0.1)/(0.1 + d**2)
    else:
        return 0 
    
def distance(x_0, x_1, y_0, y_1):
    return math.sqrt((x_1-x_0)**2 + (y_1-y_0)**2)
    
grid_notes = [[0, 0], [0, 1], [0, 2]]
grid_weights = []
grid_f = np.zeros(len(grid_notes))

for node in grid_notes:
    f = 0
    grid_weights.append([])
    for i in range(len(x_obs)):
        dist = distance(node[0], x_obs[i], node[1], y_obs[i])
        w = weight(dist)
        grid_weights[grid_notes.index(node)].append(w)
        #print("dist: ", dist, "w: ", w)
        f_i =  f_obs[i]*w
        f = f + f_i
    grid_f[grid_notes.index(node)] = f
    

print(grid_notes)
print(grid_f)
print(grid_weights)
    
