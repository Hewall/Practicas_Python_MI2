# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 23:59:01 2022

@author: gena_
"""
import numpy as np 
import matplotlib.pyplot as plt
from math import e

#xi = float(input('Da valor inicial de xi: '))
#xf = float(input('Da valor final de xf: '))
#n = int(input('Da valor de iteraciones: '))
#yi = float(input('Da valor inicial de yi: '))

xi=0
xf=0

n=5
yi=1



x= np.zeros(n+2)
x[0] = xi

y = np.zeros(n+2)
y[0] = yi

def dydx(x,y):
    return (-2*y+((x**3)*e**-2*x))


h=0.1


i=0
while (i <= n):
    k1=dydx(x[i],y[i])
    print(k1)
    k2=dydx(x[i]+ h/2,y[i]+h*k1/2)
    print(k2)
    k3=dydx(x[i]+ h/2,y[i]+h*k2/2)
    print(k3)
    k4=dydx(x[i]+ h,y[i]+h*k3)
    print(k4)
    y[i+1] = y[i] +(h/6)*(k1+2*k2+2*k3+k4)
    print(y[i+1])
    x[i+1] = x[i]+h
    i = i + 1
    print()
    
print('Solución Aprox: ')
print(y[i-1])

x= np.delete(x,i)
y= np.delete(y,i)


plt.scatter(x,y).set_color('Blue')
plt.title('Método RK4')
plt.xlabel('Intervalo x')
plt.ylabel('y')
#plt.grid(axis='x', color='0.95')
plt.grid()