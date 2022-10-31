import numpy as np
import matplotlib.pyplot as plt


#Definir limites del grid en x
a = -5
b = 5
N = 1001 #Numero de puntos dentro del grid
#Definiendo grid en x
x = np.linspace(a,b,N)
h = x[1] - x[0]

#Calculando matriz de 2da derivada:  
def matriz_2da_dev(N):
    M = np.zeros((N-2,N-2))
    V = np.zeros_like(M)
    for i in range(N-2):
        for j in range(N-2):
            if i == j:
                M[i,j] = -2
                V[i,j] = Vpot(x[i+1])
            elif np.abs(i-j) == 1:
                M[i,j] = 1       
    return M, V

def Vpot(x, types = 0):
    if types == 0:
        return x**2
    else:
        return 0

M, V = matriz_2da_dev(N)
H = -M/(2*h**2) + V

val,vec=np.linalg.eig(H)
z = np.argsort(val)
z = z[0:4]
energies=(val[z]/val[z][0])
print(energies)

plt.figure(figsize=(12,10))
for i in range(len(z)):
    y = []
    y = np.append(y,vec[:,z[i]])
    y = np.append(y,0)
    y = np.insert(y,0,0)
    plt.plot(x,y,lw=3, label="{} ".format(i))
    plt.xlabel('x', size=14)
    plt.ylabel('$\psi$(x)',size=14)
plt.legend()
plt.title('normalized wavefunctions for a harmonic oscillator using finite difference method',size=14)
plt.show()


