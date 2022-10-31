# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 16:56:52 2021

@author: A01231793/Pedro Piña
"""

import math
import numpy as np
import matplotlib.pyplot as plt

def problema_2_2(N):
    u = np.random.uniform(0., 1.0,size=N)
    x = np.zeros(N)
    for i in range(N):
        x[i]=math.acos(1-2*u[i])
    return x
def main():
    N=10
    mean = np.zeros(5)
    std = np.zeros(5)
    for i in range(5):
        x = problema_2_2(N**(i+1))
        mean[i]=sum(x)/(N**(i+1))
        for j in range(len(x)):
            std[i]+=((x[j]-mean[i])**2)/(N**(i+1)-1)
        std[i]=math.sqrt(std[i])
    plt.plot([10,100,1000,10000,100000],mean,'ro',label='promedio')
    plt.plot([10,100,1000,10000,100000],mean)
    plt.plot([10,100,1000,10000,100000],std,'go',label='varianza')
    plt.plot([10,100,1000,10000,100000],std)
    plt.legend()
    plt.show()  
    return std,mean
std,mean=main()
