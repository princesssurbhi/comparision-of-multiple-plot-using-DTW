#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 21:02:01 2020

@author: surbhi
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def toNumbers(numbers):
    converted = []
    for number in numbers:
        converted.append(float(number))
    return converted
best = pd.read_excel('/home/surbhi/Desktop/papaer publish work/META DATA REGARDING SPEED BRAKER IDENTIFICATION/One Plus/cimented speed breaker/TWO_WHEELER_MOUNTER_26_11_2019-06_30_40_ONEPLUS A3003_150/kl_2500-2700_best.xlsx')
for i in range(1,5):
    test = pd.read_excel('/home/surbhi/Desktop/papaer publish work/META DATA REGARDING SPEED BRAKER IDENTIFICATION/One Plus/cimented speed breaker/TWO_WHEELER_MOUNTER_26_11_2019-06_28_49_ONEPLUS A3003_150/KL_200_rows_'+str(i)+'.xlsx')

    a = '\n'.join(str(e) for e in list(best['z']))
    b = '\n'.join(str(e) for e in list(test['z']))
    
    a = np.array(toNumbers(a.split('\n')))/1000
    b = np.array(toNumbers(b.split('\n')))/1000
    inf = 2**100
    
    dtw = np.zeros((a.shape[0]+1, b.shape[0]+1))
    X = np.array([[]])
    Y = np.array([[]])
    warpingCost = 0
    dtw[len(a)] = inf
    dtw[:,0] = inf
    dtw[len(a),0] = 0
    for j in range(1,b.shape[0]+1):
        for i in range(a.shape[0]-1,-1,-1):
            cost = abs(a[a.shape[0] -1 - i] - b[j-1])
            dtw[i,j] = cost + min(dtw[i+1,j], dtw[i,j-1], dtw[i+1,j-1])
    i,j = 0,b.shape[0]
    while (j>=1) and (i<=a.shape[0]-1):
        X = np.append(X,j)
        Y = np.append(Y,i)
        minimum = min(dtw[i+1,j], dtw[i,j-1], dtw[i+1,j-1])
        if minimum == dtw[i+1,j]:
            i += 1
        elif minimum == dtw[i,j-1] :
            j -= 1
        else:
            i+=1
            j-=1
    co_ordinate = []

    for i in range(len(X)):
        warpingCost += dtw[int(Y[i]),int(X[i])]
        co_ordinate.append((int(X[i]-1),a.shape[0]-1-int(Y[i])))

    print("Warping Cost =",warpingCost)
    print(str(co_ordinate))
    
    if warpingCost < 2:
        ty = 'Very Good Ride'
    elif warpingCost < 4:
        ty = 'Good Ride'
    elif warpingCost < 6:
        ty = 'Average Ride'
    elif warpingCost < 8:
        ty = 'Bad Ride'
    else:
        ty = 'very Bad Ride'
      
    
            
            
   
          
    plt.plot(X+0.5,len(a)-Y+0.5, label = ty)
    plt.xlabel('Time')
    plt.ylabel('Optimal Wrapping Distance')
    plt.legend()
    plt.title('comparision of warping distace of cimented speed-breaker')
    plt.show()


