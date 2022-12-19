import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt


t = np.array(pd.read_csv(r'exersices\Lab_6\t.csv').values.tolist())
noise = np.array(pd.read_csv(r'exersices\Lab_6\noise.csv').values.tolist())
signal = np.array(pd.read_csv(r'exersices\Lab_6\signal.csv').values.tolist())
t = np.ndarray.flatten(t)
noise = np.ndarray.flatten(noise)
signal = np.ndarray.flatten(signal)


#Load Data 
t_obs = t
obs = noise + signal
obs_nomean = obs - (sum(obs)/len(obs))


#Compute obs lag matrix 
t1, t2 = np.meshgrid(t_obs, t_obs)
TAO = abs(t1-t2)
TAO = np.triu(TAO, 1)

#Compute correspondent obs cov matrix 
p1, p2 = np.meshgrid(obs_nomean, obs_nomean)
C = p1 * p2
C = np.triu(C, 1)

#Reshape lag and cov into arrays 
tao = [] 
for i in range(len(TAO.T)):
    for j in range(len(TAO.T[i])):
          tao.append([TAO.T[i][j]])

c = [] 
for i in range(len(C.T)):
    for j in range(len(C.T)):
        c.append([C.T[i][j]])

#Consider single combinations only 


delta_tao_efc = 2
max_tao_efc = 50 
tao_ecf = np.linspace(0, delta_tao_efc, max_tao_efc)
tao_inbin = np.digitize(tao, tao_ecf)

