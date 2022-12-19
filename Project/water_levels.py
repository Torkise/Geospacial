import numpy as np 
import pandas as pd 
import math
import mean


water_levels_xlsx = pd.read_excel(r'Project\Lab_Assignment_data\water_levels.xlsx', header=None)

def get_water_ids(): 
    ids = []
    for i in range(0, 78, 3):
        ids.append(water_levels_xlsx[i][1])
    return ids 

def get_lake_measurement(id):
    id_s = get_water_ids()
    if (id not in id_s): return None
    measurement = []
    date = []
    for i in range(0, 78, 3): 
        # TODO: Finn ut hvorfor den stopper på 78. Er egt ikke så farlig da den bare skal håndtere en fil.
        if water_levels_xlsx[i][1] == id:
            date = water_levels_xlsx[i+1].tolist() 
            measurement = water_levels_xlsx[i+2].tolist()
    return date, measurement
        


def get_mean_water_level_lake(id):
    x =get_lake_measurement(id)
    return mean.mean(x) 


