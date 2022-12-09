# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 21:08:25 2022

@author: gena_
"""
#Método de Euler 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')


#definimos la ED para resolver
def dydx(x,y):
    return (x-y)

#condiciones iniciales euler
n=5
x0=0
xf=1
y0=2



#cálculo del tamaño de paso h
h=(xf-x0)/n

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

plt.scatter(x,y).set_color("green")
plt.title('ED-Método de Euler')
plt.xlabel('Intervalo x')
plt.ylabel('y')
plt.grid(axis='both', color='0.95')

