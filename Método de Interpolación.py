# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 15:11:31 2022

@author: gena_
"""

import numpy as np
import matplotlib.pyplot as plt

#sistema de ecuaciones
#x=np.array([1,2,3,4])
#y=np.array([2,6,4,10])
x = np.array([1, 2, 3, 4]).reshape(2, 2)
y = np.array([2, 4, 6, 10]).reshape(2, 2)
N=len(x)
a=np.zeros((N,N))
#b=np.zeros(N)
#b=y

#inicializamos yteo para las iteraciones
#yteo=0
yteo=0
#llenamos N columnas
# utilizamos la matriz traspuesta


#calculamos yteo
for i in range(N):
    yteo=yteo+a.T[i]*xteo**i

print(a,y)
#verifiquemos que se forme la matriz 
#print(A)
#print(A,b)

#resolvemos el sistema de ecuaciones
#en a nos regresa la ordenada y la pendiente 
a=np.linalg.solve(a,y)
print(a)

#Graficamos los datos experimentales
#plt.plot(x,y,'ro')
#calculamos la y teorica y la graficamos en azul 
#yteo= a[0]+a[1]*xteo + a[2]*xteo**2
#plt.plot(xteo,yteo,'b-')
#Graficamos el mínimo y máximo  de x con 100 datos 
xteo=np.linspace(min(x),max(x),100)

plt.plot(x,y,'ro')
plt.plot(xteo,yteo,'b-')

plt.title('Interpolación polinómica')
plt.xlabel('intervalo x')
plt.ylabel('y')
plt.legend(title='Ajute: ')
plt.grid(axis='both', color='0.95')

