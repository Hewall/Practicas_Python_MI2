# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 12:12:00 2022

@author: gena_
"""

import numpy as np
import matplotlib.pyplot as plt
from math import e

fx = lambda x: e**-x-x
dfx = lambda x: -e**-x-1


resultados = []

x0=0
tolerancia=0.001
error=abs(2*tolerancia)

np.set_printoptions(precision=4)

xi=x0
while(error >= tolerancia):
    xnuevo = xi - fx(xi)/dfx(xi)
    
    error = abs(xnuevo-xi)
    
    resultados.append([xi,xnuevo,error])
    
    xi = xnuevo
    
    plt.plot(xi,xnuevo,'o--', color='red', label=xi)

resultados = np.array(resultados)
n = len(resultados)

print(['xi', 'xnuevo', 'error'])

print(resultados)
print('Raíz = %2.4f'% xi)
print('Error= ',error)
print('Error= %2.8f'% error)

x= np.arange(-1,5)
y=fx(x)

plt.plot(x,y,'o--', color='blue', label='f(x)', alpha=0.3)
plt.title('Método de Newton-Raphson')
plt.xlabel('Intervalo x')
plt.ylabel('y')
plt.legend(title='Aproximaciones:')
plt.grid(axis='both', color='0.20')
plt.show()
             
