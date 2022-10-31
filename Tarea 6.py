import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
#Definir limites del grid en x
a = -5
b = 5
N = 1001
t = 300 #Numero de puntos dentro del grid
#Definiendo grid en x
x = np.linspace(a,b,N)
h = x[1] - x[0]
#Inicializamos la matriz de la funcion de onda en la que cada fila
#representa la funcion de onda en determinado tiempo t
psi = np.zeros((t, N), dtype=np.complex128)
sig = 1
mu = 0
#Inicializamos la funcion de onda con una onda gaussiana
psi [0] = (1./(np.sqrt(2.*np.pi)*sig)*np.exp(-np.power((x - mu)/sig, 2.)/2))/np.sqrt(0.28209479177343855)
m = 1
_lambda = 1j/(2*m)
#Definimos los vectores auxiliares que utilizaremos
u = np.zeros(N, dtype=np.complex128)
l = np.zeros(N, dtype=np.complex128)
z = np.zeros(N, dtype=np.complex128)
# Definimos una funcion de potencial que la podemos modificar con el parametro
#"types" que por default es igual a 0, osease, el poze de potencial infinito
def Vpot(x, types = 2):
    if types == 0:
        return 0
    elif types == 1:
        return (x**2)/2
    elif types == 2:
        if x < 0:
            return 0
        else: 
            return 1
    
#Definimos los vectores de la matriz diagonal
def S2(l, u):
    for i in range(1, N):
        l[i] = 1 + _lambda + 1j*Vpot(x[i])/2 + (_lambda/2) * u[i-1]
        u[i] = -_lambda/(2*l[i])
    return u, l

#Evolucionamos en el tiempo y utilizamos la reduccion de Crout para resolver
#la ecuacion diferencial
def S3(t, l, u):
    u, l = S2(l, u)
    for i in range(t-1):
        z[0] = 0
        for j in range(1, N-1):
            z[j] = ((1 - _lambda) * psi[i,j] - 1j*Vpot(x[j])/2 * psi[i,j] + (_lambda/2)
                    * (psi[i,j+1] + psi[i,j-1] + z[j-1]))/l[j]
        for k in range(N-2, -1, -1):
            psi[i+1,k] = z[k] - u[k] * psi[i+1,k+1]
        
    return psi

psi = S3(t, l, u)
#Integramos la valor absoluto cuadrado de la funcion de onda en el tiempo inicial
#y tiempo final para comparar si no hubo alguna perdida de datos
print("Integral de la funcion de onda en ti = {i}".format(i = integrate.simpson(np.square(np.abs(psi[0])), dx = h)))
print("Integral de la funcion de onda en tf = {i}".format(i = integrate.simpson(np.square(np.abs(psi[-1])), dx = h)))
plt1 = plt.plot(x, np.real(psi[0]), color = "green", lw = 3)
plt.xlabel('x', size=14)
plt.ylabel('$\psi$(x)',size=14)
plt.show()