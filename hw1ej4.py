# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 18:08:29 2021

@author: A01231793/Pedro Piña
"""

import math
import numpy as np
import matplotlib.pyplot as plt

def problema_4(N):
    j=0
    samp = np.zeros(N)
    while j<=N-1:
        y= np.random.uniform(0., 2/math.pi)
        x= np.random.uniform(0., math.pi)
        if y<=(2/math.pi)*(math.sin(x))**2:
            samp[j]=x
            j+=1
    return samp

def main():
    N=10000
    samp = problema_4(N)
    plt.hist(samp)
    plt.show 
main()