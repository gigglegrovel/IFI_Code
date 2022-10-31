# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 08:58:09 2021

@author: A01231793/Pedro Piña
"""
  
import math
import numpy as np
import matplotlib.pyplot as plt
import random
import pandas as pd
from scipy.optimize import curve_fit
 #Creamos una función que nos pueda evaluar los valores de un vector en una función, y regresarnos un vector ed valores evaluados
def fun(x,a,b):
    return (a*x)*(b**2+x**2)**(-1/2)

def metropolis(x,a,b,ydata,error,var,N):
    #creamos un valor que contenga nuestros parámetros con los que vamos a jugar
    par = [a,b]
    Ka=[a]
    Kb=[b]
    chi=[]
    #print(par)
    #evaluamos la función
    y=fun(x,par[0],par[1])
    #guardamos esos parámetros en una lista
    P=[list(par)]
    for i in range(N):
        #print(par)
        chi1 = 0
        #Sacamos chi cuadrada de nuestra función actual
        for j in range(len(y)):
            chi1+=((ydata[j]-y[j])/error[j])**2
        #print(chi1,'1')    
        #generamos un error aleatorio entre cero y nuestra variancia 
        r1=random.randrange(-1,2,2)*random.uniform(0,var) 
        #elegimos un parametro a cambiar de los parametros con el error generado
        r2=random.randint(0,1)
        par[r2]=par[r2]+r1
       # print(r1,r2)
        #print(par)
        #generamos otra función
        y=fun(x,par[0],par[1])
        #print(y)
        chi2 = 0
        #calculamos la chi cuadrada de la función
        for k in range(len(y)):
            chi2+=((ydata[k]-y[k])/error[k])**2
        #print(chi2,'2') 
        #print(chi1,chi2)
        
        #Condiciones del algoritmo de Metrópolis
        if chi2<chi1:
            P.append(par)
        elif chi2>chi1:
            r = random.uniform(0,1)
            chi.append(chi2)
           # print(chi1-chi2)
            if math.exp(-(chi2-chi1)/2)>r:
                P.append(list(par))
                Ka.append(par[0])
                Kb.append(par[1])
                chi.append(chi2)
            elif math.exp(-(chi2-chi1)/2)<r:
                par[r2]+=(-r1)
                #y=fun(x,par[0],par[1])
                P.append(list(par))
                Ka.append(par[0])
                Kb.append(par[1])
                chi.append(chi1)
                #print(P[-1])
    return P[-1] ,Ka,Kb,chi    
            

#leemos los datos del csv
p=pd.read_csv('mock_data.csv',header=0)
#asignamos un vector a cada columna
R=np.array(list(p['0']))
v=np.array(list(p['1']))
error=np.array(list(p['2']))
#res,cov = curve_fit(fun,R,v)
#print(res)

#definimos un error
perr = 1.5
#perr = sum(perr)
#algoritmo de Metropolis
P1,ka1,kb1,chi1= metropolis(R,10,3,v,error,perr,1000000)
#ploteamos puntos y ajuste


#leemos los datos del csv
#p=pd.read_csv('mock_data.csv',header=0)
#asignamos un vector a cada columna
#R=np.array(list(p['0']))
#v=np.array(list(p['1']))
#error=np.array(list(p['2']))
#res,cov = curve_fit(fun,R,v)
#print(res)

#definimos un error
perr = 1.5
#perr = sum(perr)
#algoritmo de Metropolis
P2,ka2,kb2,chi2= metropolis(R,100,13,v,error,perr,1000000)
#ploteamos puntos y ajuste
#fig,axes = plt.subplots()
#axes.scatter ( R,v)
#plt.plot(R,(P2[0]*R)*(P2[1]**2+R**2)**(-1/2),'r')
#plt.title('v0= '+str(P2[0])+', R0='+str(P2[1]))
#plt.xlabel('R')
#plt.ylabel('V')
#plt.show()

#leemos los datos del csv
#
#asignamos un vector a cada columna
#R=np.array(list(p['0']))
#v=np.array(list(p['1']))
#error=np.array(list(p['2']))
#res,cov = curve_fit(fun,R,v)
#print(res)

#definimos un error
#perr = 1.5
#perr = sum(perr)
#algoritmo de Metropolis
P3,ka3,kb3,chi3= metropolis(R,50,32,v,error,perr,1000000)
#ploteamos puntos y ajuste
fig,axes = plt.subplots()
axes.scatter ( R,v)
plt.plot(R,(P3[0]*R)*(P3[1]**2+R**2)**(-1/2),'r')
plt.title('v0= '+str(P[0])+', R0='+str(P[1]))
plt.xlabel('R')
plt.ylabel('V')
plt.show()
P4,ka4,kb4,chi4= metropolis(R,150,-5,v,error,perr,1000000)




