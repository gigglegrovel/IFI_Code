"""__________________________________________________________________________________
Proyecto Final Física Computacional

Éste código va a tratar de hacer una simulación por medio de métodos de 
Montecarlo de un gas de fermiones. La deneración del sistema está dada por 
g(n)=2n+1
Los Fermioens no pueden ocupar el mismo estado cuántico, por lo que no pueden
haber más Fermiones en un estado de energía que la degeneración del mismo.
En el equilibrio siguen la distribución de Fermi Dicar.
Se buscara simular el comportamiento de éstos y su evolución en entropía.
__________________________________________________________________________________"""
#Se importan las librerías requeridas
import math
import numpy as np
import matplotlib.pyplot as plt
import random
#Obtiene una simulación paso a paso de cómo evoluciona en el tiempo una 
#distribución energética de un número de electrones en una distribución de e
#energías, para facilidad que la distribución sea un arreglo NUMPY, y el número
#de iteraciones que correremos
def fermion(dist,N):
    #Creamos un vector de energías
    E=np.linspace(0,len(dist)-1,len(dist))
    #generamos una lista de degeneración
    g=np.zeros(len(dist))
    
    for i in range(len(dist)):
        g[i]+=(2*i+1)
        #generamos una matriz donde guardar nuestros estados
    D = [list(dist)]
    P=[]
    i=0
    #Empezamos la simulación
    
    while i<=N:
        dist1 = list(dist)
        #Generamos dos números aleatorios
        r1 = random.randrange(0,len(dist))
        r2= random.randrange(0,len(dist))
        #checamos que no sean iguales, no esté vacío el nivel de energía
        # y que no se rompa la degeneración
        
        if abs(r1-r2)>0 and dist[r1]>0 and dist[r2]<g[r2]:
            #Movemos el Fermion a otro nivel de energía
            dist[r1]+=-1
            dist[r2]+=1
            #Sacamos la diferencia de energía del Fermion
            dE = E[r2]-E[r1]
            Ep=abs(dE)
            #Iniciamos la redistribución de los Bosones en el sistema para 
            #así mantener la energía constante
            
            while Ep>0:
                #print("Check 1")
                #Redistribución para cambios positivos de energía
                
                if np.sign(dE)==1:
                    rn_2 = random.randrange(0,math.trunc(math.log(Ep,2))+1)
                    rn = random.randrange(2**rn_2,len(dist))
                    #Como cada numero podemos descomponerlo en binario, la 
                    #redistribución se descompone de igual manera en binario
               #     print("Check 2")
                    
                    if dist[rn]>0 and dist[rn-2**rn_2]<g[rn-2**rn_2] :
                        Ep+=(-2**rn_2)
                        dist[rn]+=(-1)
                        dist[rn-2**rn_2]+=1
              #          print("Check 3")
                #mismo proceso para energías negativas
                
                if np.sign(dE)==-1:
                    rn_2 = random.randrange(0,math.trunc(math.log(Ep,2))+1)
                    rn = random.randrange(0,len(dist)-2**rn_2)
             #       print("Check 2")
                    if dist[rn]>0 and dist[rn+2**rn_2]<g[rn+2**rn_2] :
                        Ep+=(-2**rn_2)
                        dist[rn]+=(-1)
                        dist[rn+2**rn_2]+=1
            #            print("Check 3")
            #Empezamos un algoritmo de Montecarlo
           # print("Check 4")
            rand_n= random.uniform(0,1)
            #Calculamos "probabilidades" con la probabilidad dada para
            #Bosones
            p1 =  1
            
            for k in range(len(dist)):
                p1*=(math.factorial(g[k]))/(math.factorial(dist[k])*math.factorial(g[k]-dist[k]))
           
            k=0 
            p2 =  1
            
            for k in range(len(dist)):
                p2*=(math.factorial(g[k]))/(math.factorial(dist1[k])*math.factorial(g[k]-dist1[k]))
            
            if p1/p2>rand_n:
                P.append(abs(math.log(p1)))
                #Guardamos la distribución en una fila matricial
                D.append(dist)
           
            else:
                P.append(abs(math.log(p2)))
                dist=list(dist1)
                #Guardamos la distribución en una fila matricial
                D.append(dist1)
                
            i+=1 
       
    return   P,D    
            

dist=[0,0,0,0,0,0,0,0,0,0,20,0,0,0,0,0]
P,D=fermion(dist,10000)

pos = range(len(dist))
    
time=np.linspace(0,10000,51)
for i in range(50):
    plt.ylim(0,sum(dist)/2)
    bar1 = plt.bar(pos, D[int(time[i])])
    plt.xlabel('Nivel de Energía')
    plt.ylabel("Número de Particulas")
    plt.pause(.0001)
    plt.show(bar1)    

S= []
for i in range(len(D)):
    B=0
    for j in range(len(dist)):
        if D[i][j]>0:
            B+=D[i][j]*math.log(D[i][j])
    S.append(sum(dist)*math.log(sum(dist))-B)
plt.plot(S)
plt.xlabel('t', size=14)
plt.ylabel('J/K',size=14)
plt.legend()
plt.title('Entropía Fermiónes',size=14)
plt.show()