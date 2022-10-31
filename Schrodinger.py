# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 12:22:12 2021

@author: End User
"""
import math
import numpy as np
import matplotlib.pyplot as plt
import random
import pandas as pd

N=2**12
x = np.linspace(-2,2,N)
h = x[1]-x[0]

def pot(x):
    return 0

T = np.zeros((N-2)**2).reshape(N-2,N-2)
V = np.zeros((N-2)**2).reshape(N-2,N-2)

for i in range(N-2):
    for j in range(N-2):
        if i == j:
            T[i][j]=-2
            V[i][j]=pot(x[i+1])
        elif np.abs(i-j)==1:
            T[i][j]=1
            V[i][j]=0
        else:
            T[i][j]=0
            V[i][j]=0 

H = -T/(2*h**2) + V

eig,eigv=np.linalg.eig(H)

z = np.argsort(eig)
z = z[0:4]

plt.figure(figsize=(12,10))
for i in range(len(z)):
    y = []
    y = np.append(y,eigv[:,z[i]])
    y = np.append(y,0)
    y = np.insert(y,0,0)
    plt.plot(x,y,lw=3, label="{} ".format(i))
    plt.xlabel('x', size=14)
    plt.ylabel('$\psi$(x)',size=14)
plt.legend()
plt.title('Estado con potencial armónico',size=14)
plt.show()

