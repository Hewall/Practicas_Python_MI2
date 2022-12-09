# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 23:23:36 2022

@author: gena_
"""
#Método de Euler 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')


#Función en donde insertamos la ED para su resolución 
def f(x,y):
    return (x-y)

#condiciones iniciales euler mejorado
x = float(input('Da valor inicial de x: '))
xf = float(input('Da valor final de x: '))
y = float(input('Da valor inicial de y: '))

#leemos n, ñpara qye quede más claro lo manejamos
#como subintervalos o número de iteraciones:
it = int(input('Da el número de subintervalos(iteraciones): '))

#inicializamos los vectores para registrar los valores de x,y (xV,yV)
# llenamos el vector con ceros 
xV = np.zeros(it+1)
#valor inicial x
xV[0]=x

yV = np.zeros(it+1)
#valor inicial y
yV[0]=y


#Paso 1 Calculamos los valor de h
h= (xf-x)/it
#calculamos los valores de x+h
for i in range(it):
    xV[i+1] = xV[i] + h
    
#Paso 2 y 3 
for i in range(0,it):
    # Paso 4 PREDICTOR valor temporal
    ft = yV[i] + h*(f(xV[i],yV[i]))
    #Paso 5 Corrector
    yV[i+1] = yV[i] + h*( (f(xV[i],yV[i])+ f(xV[i+1],ft))/2 )
    #Paso 6 y 7 -el incremento x+h ya esta en el vector x,
    #solamente tomamos  el valor para la siguiente
print()

#Paso 8 imprimir resultado
print('Resultado: ')  #print o imprime xV

#Creamos una lista con el arreglo yV
nlist = list()
for i in yV:
    nlist.append(i)
for i in nlist:
    print(i) # print o imprime (yV)

#condiciones iniciales
n=5
x0=0
xf=1
y0=2

#cálculo del tamaño de paso h
h=(xf-x0)/n

#definimos la ED para resolver
def dydx(x,y):
    return (x-y)

#Inicializamos arreglo(x,y)
x=[x0]
y=[y0]

#Iteraciones
for i in range(n):
    print(i)
    y0= y0 + h*dydx(x0,y0)
    y.append(y0)
    x0=x0+h
    x.append(x0)
    print(x0,y0)
print(x)
print(y)



plt.plot(xV, yV, 'o--', color='red', label='Euler Mejorado', alpha=0.3)
plt.plot(x, y, 'o--', color='green', label='Euler', alpha=0.3)

plt.grid(axis='x', colors='0.95')
plt.legend(title='Resultados')
plt.title('Euler VS Euler Mejorado')
plt.show()