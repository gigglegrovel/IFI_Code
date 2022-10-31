# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 16:52:02 2022

@author: End User
"""

import numpy as np
from scipy.spatial.distance import pdist, squareform
import math

a  = 3.625*10**-10
a1 = a/2*np.array([1,1,0])
a1 = np.transpose(a1)
a2 = a/2*np.array([0,1,1])
a2 = np.transpose(a2)
a3 = a/2*np.array([1,0,1])
a3 = np.transpose(a3)

l = np.array(range(-10,11))
X,Y,Z = np.meshgrid(l,l,l)
caca = np.array([np.transpose(X.flatten()),np.transpose(Y.flatten()),np.transpose(Z.flatten())])
caca2= np.array([a1,a2,a3])
c = np.matmul(caca2,caca)
c = np.transpose(c)
t = np.linspace(0,47,470)
t1 = np.deg2rad(t)
lam = 1.5405*10**-10
Q = 4*math.pi*np.sin(t1)/lam
I = np.zeros(len(t1))
r = squareform(pdist(c))

a0 = np.array([13.338 ,7.1676, 5.6158 ,1.6735])

b0 = np.array([3.5828,0.247,11.3966,64.8126])

c0 = 1.191

f = np.zeros(len(Q))

for i in range(len(Q)):
    f[i]= sum(a0*np.exp(-b0*((Q[i])/(4*math.pi))**2))+c0
#%%
N = len(c)

bins = 40000

nk,rk = np.histogram(r,bins)
#%%
for i in range(1,len(Q)):
    s = 0
    for j in range(bins):
        if rk[j]==0:
            s=s+nk[j]
        else:
            s=s+nk[j]*math.sin(Q[i]*rk[j])/(Q[i]*rk[j])
    I[i]=(f[i]**2)*(N+2*s)

#%%
def matfind(list,el):
    index = []
    for i in range(len(list)):
        if list[i]==el:
            index.append(i)
    return index

# %%
t = t[150:]
# %%
I = I[150:]
# %%
import matplotlib.pyplot as plt
plt.plot(2*t,I)
# %%
