import numpy as np 
import matplotlib.pyplot as plt 
import math

x_obs = [-1, -1/2, 1, 0.2]
y_obs = [1, 1/2, 1, 0.3]
f_obs = [1, 3, 2, 1]

def weight(d):
    if d <= 1:
        return (1/10)/((1/10)+d**2)
    else:
        return 0 
    
def distance(x_0, x_1, y_0, y_1):
    return math.sqrt((x_1-x_0)**2 + (y_1-y_0)**2)

def grid_var(variance, weights):
    if(sum(weights) == 0): return 0
    return (variance*sum([w**2 for w in weights ]))/(sum(weights)**2)
    
grid_nodes = [[0, 0]]
grid_weights = []
grid_dist = []
grid_f = np.zeros(len(grid_nodes))

for node in grid_nodes:
    f = 0
    w = 0
    grid_weights.append([])
    grid_dist.append([])
    for i in range(len(x_obs)):
        dist = distance(node[0], x_obs[i], node[1], y_obs[i])
        w_i = weight(dist)
        grid_dist[grid_nodes.index(node)].append(dist)
        grid_weights[grid_nodes.index(node)].append(w_i)
        if w_i > 0:
            f = f + f_obs[i]*w_i
            w = w + w_i
    
    if w == 0: grid_f[grid_nodes.index(node)] = 0
    else: grid_f[grid_nodes.index(node)] = f/w
    


print("Grid Notes\n", grid_nodes)
for i in range(len(grid_nodes)):
    print("Grid Node", grid_nodes[i])
    print("Distances \n", grid_dist[i])
    print("Weights: ", grid_weights[i])
    print("F_val", grid_f)
    
#Define Variance 
variance = 0.01
for i in range(len(grid_nodes)):
    print("Var for Node", grid_nodes[i], ": ",grid_var(variance, grid_weights[i]))
    
