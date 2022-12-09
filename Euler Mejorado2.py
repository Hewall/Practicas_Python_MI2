# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 21:36:26 2022

@author: gena_
"""

import numpy as np
import matplotlib.pyplot as plt

#Solicitamos al usuario las condiciones iniciales 
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

#Función en donde insertamos la ED para su resolución 
def f(x,y):
    return (x-y)

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
    
#Se Gráfica el resultado
plt.scatter(xV,yV).set_color("blue")
plt.title('ED - Método de Euler Mejorado')
plt.xlabel('Intervalo x')
plt.ylabel('y')
plt.grid()


    
    
    