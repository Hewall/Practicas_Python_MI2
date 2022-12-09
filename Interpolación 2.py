# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 10:13:11 2022

@author: gena_
"""

import numpy as np 
import matplotlib.pyplot as plt

#sistema de matrices
x=np.array([1,2,3,4,]) 
y=np.array([2,4,6,8])
N=len(x) 
a=np.zeros((N,N)) 


for i in range(N):
    a.T[i]=x**i

print(a,y) 

a=np.linalg.solve(a,y) 
print(a) 

xteo=np.linspace(min(x),max(x), 100) 

yteo=0

for i in range(N):
    yteo=yteo+a[i]*xteo**i
 
plt.plot(x,y, 'ro')
plt.plot(xteo,yteo, 'b-')

plt.title('Interpolacion Polinómica')
plt.xlabel('Intervalo x')
plt.ylabel('y')
plt.legend(title='Ajuste: ')
plt.grid(axis='both', color='0.95')