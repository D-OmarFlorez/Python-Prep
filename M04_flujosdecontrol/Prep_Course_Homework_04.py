#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:

from ast import Str
from socketserver import ThreadingUnixStreamServer
from unittest.util import strclass


a= 3
if( a >0):
    print('la variable es un numero entero mayor que cero')
elif(a==0):
    print('la variable es igual a 0')
else:
    print('la variable no es un numero entero')


# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:

a= 3
b='3'
if (type(a)==type(b)):
    print('las variables son de el mismo tipo')
else:
    print('las variables no son de el mismo tipo')

# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:

for c in range(0, 21):
    if (c % 2 ==0):
        print('el numero es par',str(c))
    else:
        print('el numero es impar',str(c))
        




# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:

c=0
for c in range (0, 6):
    c+=1
    print('el valor de ',str(c),'y su elevacion a la 3° potencia es ', str(c**3))



# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:
a=4
for a in range(0, a):
    a+=1
    print (' el ciclo se repite por',str(a),'vez')



# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:

a= 7
if (type(a)==int):
    if (a>0):
        f=a
        while(a>2):
            a= a-1
            f=f*a
        print('el factorial es',str(f))

    else:
        print('el factorial no es mayor que cero')
else:
    print('el factorial no es un numero entero')



# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:
a=0
while (a<4):
    a+=1
    for i in range(1,a):
        print('el ciclo while n°', str(a))
        print('el ciclo for n°', str(i))


# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:
x=5
for a in range(0,x):
    a+=1
    if (a>8):
        break
    while(x<6):
        x-=1
        if(x<0):
            break
        print('el ciclo for n°',str(a))
        print('el ciclo while n°', str(x))



# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:

a= 0
b=30
c=True
while(a< b):
    for x in range (2,a):
        if(a % x == 0):
            c=False
    if (c):
        print(a)
    else:
        c=True
    a+=1
    if(a>30):
     break



# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:

a=0
b=30
c=True
while(a<b):
    for x in range(2,a):
        if (a % x ==0):
            c=False
            break
    if (c):
        print(a)
    else:
        c=True
    a+=1 


# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:
sinbreak= 0
a = 0
b=30
p= True
while (a < b):
    for x in range(2, a):
        sinbreak += 1
        if (a % x == 0):
            p= False
    if (p):
        print(a)
    else:
        p = True
    a += 1
print('ciclos en total: ' + str(sinbreak))
# In[57]:

conbreak= 0
sinbreak=0
a = 0
b=30
p= True
while (a < b):
    for x in range(2, a):
        sinbreak += 1
        if (a % x == 0):
            p= False 
    for x in range(2, a):
        conbreak += 1
        if (a % x == 0):
            p= False
            break
    if (p):
        print(a)
    else:
        p = True
    a += 1
print('ciclos en total: ' + str(conbreak))
print('se optimizo un:',str(conbreak/sinbreak),'% de ciclos')
#aqui lo repeti como en la actividad resuelta pero me da error de que no declare la variable
#'sinbreak, por lo que tuve que reacer la operacion en esta celula

# 12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?

# In[58]:

conbreak= 0
sinbreak=0
a = 0
b= 70
p= True
while (a < b):
    for x in range(2, a):
        sinbreak += 1
        if (a % x == 0):
            p= False  #tuve que volver a declarar la variable 'sin break' para que me la reconociera pues no la descargo
    for x in range(2, a):
        conbreak += 1
        if (a % x == 0):
            p= False
            break
    if (p):
        print(a)
    else:
        p = True
    a += 1
print('ciclos en total: ' + str(conbreak))
print('se optimizo en un',str(conbreak/sinbreak),  '% de ciclos')




# In[59]:




# 13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:
a=100
while(a<=300):
    a+=1
    if (a % 12 ==0):
        print('el numero',str(a), 'es divisible por 12')
        continue 
        


# 14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:
a=0
b=30
c=True
while(a < b):
    for x in range (2,a):
        if(a % x == 0):
            c=False
            break
    if(c):
        print(a)
        print('desea ver el siguiente numero primo?')
        if(input() != 'yes'):
         print('fin del programa')
         break
    if (c):
        print(a)
    else:
        c=True
    a+=1
    if(a>30):
     break
  





# 15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:

a=99
while( a<300):
    a+=1
    if (a % 3==0): 
        print('el numero ',str(a),'es divisible por 3' )
        break
    #estos ultimos los pude hacer sin mirar los otros ejercicios :)


# %%
