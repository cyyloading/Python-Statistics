# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 01:25:44 2022

@author: cyy
"""

#Simulate multiple random walks 
# Random work
# roll dice: if number=1 or 2,move back 1 step; if number=3 or 4 or 5,move forward 1 step;
# if number = 6, roll the dice again, get a number j, and move forward j steps

import numpy as np
import matplotlib.pyplot as plt


all_walks = []

for i in range(20):  # simulate 20 times
    # initialize random walk
    random_walk = [0]
    
    for j in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        
        if dice<=2:
            step = max(0,step-1)  # the minimum walk location is in 0
        elif dice<=5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)  # roll the dice again
        
        random_walk.append(step)
    all_walks.append(random_walk)
    
# convert all_walks to numpy array
np_all_walks = np.array(all_walks)
# Transpose np_all_walks
np_all_walks_T = np.transpose(np_all_walks)

plt.plot(np_all_walks_T)
plt.xlabel('times of rolling dice')
plt.ylabel('location')
plt.show()