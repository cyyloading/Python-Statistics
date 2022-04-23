# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 01:08:18 2022

@author: TA005
"""

# Random work
# roll dice: if number=1 or 2,move back 1 step; if number=3 or 4 or 5,move forward 1 step;
# if number = 6, roll the dice again, get a number j, and move forward j steps

import numpy as np
import matplotlib.pyplot as plt

# initialize random walk
random_walk = [0]

for i in range(100):
    step = random_walk[-1]
    dice = np.random.randint(1,7)
    
    if dice<=2:
        step = max(0,step-1)  # the minimum walk location is in 0
    elif dice<=5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)  # roll the dice again
    
    random_walk.append(step)
    
plt.plot(random_walk)
plt.xlabel('times of rolling dice')
plt.ylabel('location')
plt.show()