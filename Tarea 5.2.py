import numpy as np
import matplotlib as plt

### Point & Shoot

#Definir limites del grid en x
a = -5
b = 5
N = 1001 #Numero de puntos dentro del grid
#Definiendo grid en x
x = np.linspace(a,b,N)
h = x[1] - x[0]
E = 1
dE = .1
psi = np.zeros(len(x))
psi[0] = 1
psi[-1] = 1

def Vpot(x, types = 0):
    if types==0:
        return x**2
    else: 
        return 0
    
def Point_Shoot(N, h, E, dE):
    i = 1
    Id = 0
    while i < N-1:
        psi[i+1] = 2*psi[i-1] -2*(E-Vpot(i*h))*(h**2)*psi[i]
        if abs(psi[i+1]) > 2:
            break
        if psi[i+1] > 0:
            div = 1
        else:
            div = -1
        if div*Id<0:
            dE = -.5*dE
        else:
            E += dE
        Id = div
        print(psi)
    
    
    