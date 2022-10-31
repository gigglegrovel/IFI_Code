# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 08:58:09 2021

@author: A01231793/Pedro Piña
"""
  
import math
import numpy as np
import matplotlib.pyplot as plt
import random
#Definimos una función que nos permita generar spins aleatorios
def spin(N):
    a = []
    for i in range(N):
        a.append((1/2)*random.randrange(-1,2,2))
    return a    
#definimos una función que nos permita calcular la energía de una configuración de spins
def energy(spin):
    J=0.2
    B=1
    gub=.33
    sisi1=0
    for i in range(len(spin)-1):
        sisi1+=spin[i]*spin[i+1]
    E= -J*sisi1-gub*B*sum(spin)
    return E
#Algoritmo de metropolis para spins aleatorios, se itera n veces
def metropolis(N,n,T):
    a = spin(N)
    #guardamos los estados en una matriz que expandimos
    estados=[list(a)]
    k=1
    #print('Energía inicial:',energy(a))
    #Empezamos las iteraciones
    for i in range(n):  
        E1=energy(list(a))
        rn = random.randint(0,N-1)
        a[rn]=-a[rn]
        E2=energy(list(a))
        if E2>E1:
            r = np.random.uniform(0,1)
            R= math.exp((E2-E1)/(k*T))
            if R<=r:
                a[rn]=-a[rn]
        estados.append(list(a))  
    #print('Energía final:',energy(a))
    return a,estados
#Algoritmo de metropolis para una configuración de spins positivos
def metropolis2(n):
    a = [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]
    estados=[list(a)]
    T = .01
    k=1
    for i in range(n):  
        E1=energy(list(a))
        rn = random.randint(0,len(a)-1)
        a[rn]=-a[rn]
        E2=energy(list(a))
        if E2>E1:
            r = np.random.uniform(0,1)
            R= math.exp((E2-E1)/(k*T))
            if R<=r:
                a[rn]=-a[rn]
        estados.append(list(a))        
    return a,estados

def main2():
    a,estados=metropolis(20,400)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.imshow(estados,origin='lower')
    ax.set_aspect('equal', adjustable='box')

    print(a.count(-.5),a.count(0.5))

def main():
    a,estados=metropolis(20,4000,5000)
    fig, ax = plt.subplots(figsize=(6,6))
    plt.xlabel('N de átomo * 200')
    plt.ylabel('Iteración')
    ax.imshow(estados, origin='lower',cmap=plt.cm.Reds, interpolation='none', extent=[0,4000,0,4000])
    ax.set_aspect(2)                
    print(a.count(-.5),':Spin antiparalelos',a.count(0.5),':Spins paralelos')    
main()    
