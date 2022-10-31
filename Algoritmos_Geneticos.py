import math
import numpy as np
import matplotlib.pyplot as plt
import random
import pandas as pd
#Definimos una función que evalue los coeficientes obtenidos
def fun(a,b,c,d,e,x):
    return a*x**4+b*x**3+c*x**2+d*x+e
   #función de aptitud 
def aptitud(poblacion,yr,x,std):
    apt = np.zeros(len(poblacion))
    for i in range(len(poblacion)):
        chi = 0
        #generamos una función con nuestros coeficientes
        y = fun(poblacion[i][0],poblacion[i][1],poblacion[i][2],poblacion[i][3],poblacion[i][4],x)
       #Evaluamos la aptitud de la función
        for j in range(len(poblacion[i])):
            chi+=((yr[j]-y[j])/std[j])**2
        apt[i]=1/chi    
    return apt   

def p_seleccion(poblacion,apt,n_padres):
    padres=np.array([[1,1,1,1,1]])
    p = list(poblacion)
    ap = list(apt)
    for j in range(n_padres):
        #suma de la aptitud
        s = sum(ap)
        #Generamos un numero aleatorio entre cero y la suma de las aptitudes
        rn = random.uniform(0,s)
        i=0
        s_p=0
        #algoritmo de selección visto en clase
        while rn>=s_p and i<len(p)-1:
            s_p+=apt[i]
            i+=1
            #para evitar copiar al mismo padre dos veces, eliminamos al padre del vector p, y su aptitud del vector ap
        padres=np.append(padres,[p[i]],axis=0)
       # p.pop(p.index(p[i]))
        p=np.delete(p,i,axis=0)
        #ap.pop(ap.index(ap[i]))
        ap=np.delete(ap,i,axis=0)
    
    padres=np.delete(padres,0,axis=0)
    rasd = random.uniform(0,1)
    for j in range(len(p)):
        if rasd >=0.1:
            rn1 = random.randrange(0,len(p[0]))
            rn2 = random.randrange(0,len(p[0]))
            a = p[j][rn1]
            b = p[j][rn2]
    return padres,p

def cruce(padres,cruce):
    crias=np.array(padres)
    for i in range(0,len(padres)-1,2):
#intercambio de genes
        temp1 = np.array(crias[i][0:cruce])
        temp2 = crias[i+1][0:cruce]
        crias[i][0:cruce] = temp2
        crias[i+1][0:cruce] = temp1
    return crias

poblacion = np.array([[3, -9, -39, -102, 180],
[-9, -6, -73, -19, -905],
[-4, 14, 76, 130, 991],
[-9, 12, 53, 131, 20],
[-10, 19, -20, 171, 501],
[8, 9, 6, -56, -246],
[-4, -8, -33, 117, -431],
[4, -4, 48, 122, -278],
[-2, 7, -43, -32, -127],
[1, 6, 88, -96, 839],
[-3, 13, -76, -61, 301],
[-5, 0, -1, -38, -320],
[0, 19, -13, 68, -80],
[1, 4, -43, 96, 290],
[0, 14, 59, 36, 71],
[-7, -2, 48, 96, -502],
[-3, -7, -81, 89, -462],
[-5, 17, -2, -41, 745],
[-1, 19, 16, -93, -823],
[-6, 16, -25, 155, -564],
[1, 4, -90, -195, -407],
[-8, -10, -100, 68, 238],
[5, 15, -92, 1, 358],
[-3, 17, -44, -172, 127],
[4, -10, 46, -190, 996],
[-8, 16, 35, -123, -426],
[-8, 12, -51, -127, 685],
[-9, 1, -70, 175, 583],
[8, 18, -84, -17, 217],
[-8, -7, -6, 142, 733],
[2, 10, 6, 138, -657],
[-1, 19, 57, -136, -485],
[6, 3, -13, 31, 315],
[-1, 1, 29, 185, -381],
[1, 9, -8, 152, 498],
[9, 13, -41, 57, 695],
[-6, -10, -22, 16, -265],
[7, 15, -89, 153, 444],
[-6, 5, 44, 22, -512],
[-8, 17, -98, -86, 710],
[-8, 6, -79, 150, 243],
[8, 19, -69, -32, -604],
[5, 11, -2, 10, -993],
[1, -8, 43, -85, -273],
[5, -3, 85, -81, 729],
[-1, 17, -55, 109, 24],
[1, 3, -19, 151, -427],
[-8, 4, -64, -21, 70],
[3, 16, -93, -126, 297],
[-9, 17, -66, -85, 721],
[-1, 11, 94, -66, 652],
[-7, 17, 96, 122, 682],
[6, -9, 21, -114, 383],
[-7, -3, -34, 197, 880],
[-5, 13, 62, -168, 759],
[-3, 13, -64, 33, 634],
[7, 17, 85, -159, 303],
[3, 11, -72, 8, -14],
[2, 9, -61, 101, -442],
[0, 9, -4, 10, 610],
[8, -9, 80, 159, -16],
[2, -4, 3, -56, 990],
[0, 0, 1, 193, -735],
[7, -9, -47, -80, 632],
[-3, 19, -37, 4, 769],
[-7, 0, -88, 22, -264],
[-7, 15, 24, 193, 431],
[-1, 8, 31, 102, -893],
[3, -5, -62, 160, -577],
[-6, 10, -57, -90, 508],
[9, 13, -67, -108, 49],
[6, -10, -10, -37, 469],
[0, -3, -83, 118, -473],
[5, -9, 18, 21, -371],
[-9, -9, -60, 5, -41],
[-6, 18, -28, -99, 408],
[-3, -7, -56, -189, -555],
[-8, -10, 37, -179, 788],
[-5, 9, 9, 85, 80],
[7, -1, -22, -197, -278],
[-3, 16, -99, -170, 235],
[9, 18, 37, 126, -343],
[-3, 18, 28, 34, 129],
[7, -7, -31, -23, 940],
[-10, 9, 32, -129, 132],
[4, 17, -89, -173, 446],
[2, -1, 2, 51, -774],
[-1, 10, 52, 189, 270],
[3, -8, -65, -100, -364],
[-9, 9, -50, 146, -593],
[0, -2, -92, 66, -853],
[1, 4, -87, -168, 776],
[0, -9, 40, 181, -141],
[9, 5, -9, 23, -422],
[-3, 18, 37, 192, 791],
[-1, -2, -13, 68, -745],
[-9, -8, -87, -40, -737],
[1, 1, 12, 126, -554],
[-3, -2, -25, -63, -102],
[7, 6, 91, -173, 634],
[-3, -6, 25, -134, 777],
[-10, 6, -64, 151, -261],
[-7, 11, -12, 144, -730],
[7, 9, -4, -157, 862],
[8, 6, 26, -107, -346],
[-5, 15, -59, 33, 168],
[7, 2, -73, 39, 784],
[-5, -8, 68, 132, 303],
[7, 15, -60, 85, 280],
[-4, -8, 9, -53, 728]])

p=pd.read_csv('mock_data_ga.csv',header=0)
    #asignamos un vector a cada columna
x=np.array(list(p['Column1']))
yr=np.array(list(p['Column2']))
error=np.array(list(p['Column3']))
std = np.zeros(len(x))+10
for i in range(100000):
    apt = aptitud(poblacion,yr,x,std)
    padres,mut= p_seleccion(poblacion,apt,4)
    crias=cruce(padres,2)
    poblacion = np.append(padres,mut,axis=0)
    z = np.argsort(apt)
    for i in range(len(crias)):
        poblacion[z[i]]=crias[i]
apti=aptitud(poblacion,yr,x,std)
z=np.argsort(apti)
fig,axes = plt.subplots()
axes.scatter ( x,yr)
plt.plot(x,fun(poblacion[z[-1]][0],poblacion[z[-1]][1],poblacion[z[-1]][2],poblacion[z[-1]][3],poblacion[z[-1]][4],x),'r')
plt.title('ajuste')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
    
    
    
    