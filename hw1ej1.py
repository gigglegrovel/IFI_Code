# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 09:19:02 2021

@author: Pedro Piña
"""

import math
import numpy as np
import matplotlib.pyplot as plt

def problema_1_1():
    N = 6
    CDF = np.zeros(7)
    for i in range(N+1):
        if i== 0:
            CDF[i]=0
        elif i>0:    
            CDF[i]=1/N+CDF[i-1]
    return CDF

def problema_1_2(x,N,PDF):
    CDF = np.zeros(len(PDF))
    sample = np.zeros(N)
    u = np.random.uniform(0., 1.0, size=N)
    j=0
    k=0
    for i in range(len(CDF)+1):
        if i == 0:
            CDF[i]=PDF[i]
        elif i>0 and i<=(len(PDF)-1):
            CDF[i]= PDF[i]+CDF[i-1]
            
    while k<=(len(u)-1):
        j=0
        found=False
        while not found and j<=(len(CDF)-2):  
            found = u[k]>= CDF[j] and u[k]<CDF[j+1]
            if found:
                sample[k]=x[j]
            j+=1    
        if not found :
            sample[k]=x[-1]
        k+=1    
    return sample

def main():
    PDF = np.array([1,1,1,1,1,1])/6
    N= 10
    x=np.array([1,2,3,4,5,6])
    mean = np.zeros(5)
    std=np.zeros(5)
    for i in range(5):
        samp = problema_1_2(x, N**(i+1), PDF)
        mean[i]=sum(samp)/(N**(i+1))
        for j in range(len(samp)):
            std[i]+=((samp[j]-mean[i])**2)/(N**(i+1)-1)
        std[i]=math.sqrt(std[i])
    plt.plot([10,100,1000,10000,100000],mean,'ro',label='promedio')
    plt.plot([10,100,1000,10000,100000],mean)
    plt.plot([10,100,1000,10000,100000],std,'go',label='varianza')
    plt.plot([10,100,1000,10000,100000],std)
    plt.legend()
    plt.show()    
main()