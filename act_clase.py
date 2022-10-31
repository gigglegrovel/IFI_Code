#-*- coding: utf-8 -*-
"""
Created on Thu Aug 26 08:58:09 2021

@author: A01231793/Pedro Piña
"""

import math
import numpy as np
import matplotlib.pyplot as plt
import random

def r_walk(L,dim,steps):
   pos=np.zeros((steps,dim))
   for i in range(steps-1):
       for j in range(dim):
           step=random.randint(-1,1)*abs(L)
           pos[i+1,j]=pos[i,j]+step
   return pos       
           
pos=np.array(r_walk(1,2,10000))

plt.plot(pos[:,0],pos[:,1])
