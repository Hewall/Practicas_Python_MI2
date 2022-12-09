# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 09:19:18 2022

@author: gena_
"""

#Derivación numérica
#Primera derivada
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return(3*x**3 + 2*x**2 + 5*x + 1)

N=11
a=-2
b=2

x = np.linspace(a,b,N)

dx=(b-a)/(N-1)

y=f(x)

#graficamos
plt.plot(x,y,'g-')
plt.title('cubica')
plt.show()

ypp=np.zeros_like(x)

for i in range(N):
    if i ==0:
        ypp[i]=(y[i+2] - 2*y[i+1] + y[i])/dx**2
    elif i==N-1:
        ypp[i]=(y[i] - 2*y[i-1] + y[i-2])/dx**2
    else:
        ypp[i]=(y[i+1] - 2*y[i] + y[i-1])/dx**2
    
def fp(x):
    return(9*x**2 + 4*x +5)
def fpp(x):
    return(18*x + 4)

plt.plot(x,fpp(x),'g-')
plt.plot(x,ypp,'bo')
plt.show()