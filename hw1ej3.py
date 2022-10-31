# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 16:09:39 2021

@author: End User
"""

import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def problema_3(N,R,h):
    r=np.zeros(N)
    ru= np.random.uniform(0., 1.0,size=N)
    theta = np.zeros(N)
    thetau= np.random.uniform(0., 1.0,size=N)
    z=np.zeros(N)
    zu= np.random.uniform(0., 1.0,size=N)
    for i in range(N):
        r[i]=math.sqrt(ru[i])*R
        theta[i]=2*math.pi*thetau[i]
        z[i]=(zu[i]-1/2)*h
    return r,theta,z
def main():
    N=100000
    R=1
    h=1
    r,theta,z=problema_3(N,R,h)
    v=np.zeros((N,3))
    for i in range(N):
        v[i,0]=r[i]*math.cos(theta[i])
        v[i,1]=r[i]*math.sin(theta[i])
        v[i,2]=z[i]
    x=v[:,0]
    y=v[:,1]
    z=v[:,2]
    #fig = plt.figure()
    #ax = fig.add_subplot(111, projection='3d')
    #ax.scatter(x,y,z)
    R=np.linspace(0,1,num=100)
    samp = np.zeros(100)
    j=0
    i=0
    for j in range(100):
        for i in range(len(r)):
            if R[j]>=r[i]:
                samp[j]+=1
    for k in range(100):
        samp[k]=samp[k]/(4*math.pi*(R[k])**2)
    plt.plot(R,samp)
    plt.show()
                
            
main()