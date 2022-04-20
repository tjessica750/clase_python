# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 14:20:23 2022

@author: USER
"""

# Variables

a = 3
print(type(a))
a = "hola"
print(type(a))
a = 3.5
print(type(a))
a = True
print(type(a))

print('Hola Mundo')
print('Hola Mundo dos')

print("I can't do it")
print('His name is "Roberto"')

# Operaciones

#suma
a = 5
b = 2
c = a + b
print(c)

#resta
a = 5
b = 2
c = a - b
print(c)

# multiplicación
a = 5
b = 2
c = a * b

# división
a = 4
b = 2
c = a / b

# división parte entera

a = 5
b = 2
c = a//b
print(c)

# Potencia
a = 2
c = a ** 6

# Raiz cuadrada
a = 16
b = a ** (1/3)

import math
raiz = math.sqrt(a)
print(raiz)

# Tipos de datos

# String str

a = "Hola Mundo"
a = 'Hola Mundo'
b = " I can't do it"
c = 'Alias "Roberto"'

# Entero int
a = 5

# Decimal float
a = 5.6

# Booleano bool
x = True
y = False

# Conversiones entre tipos de datos

# Convertir de x a entero

a = '3'
b = int(a)
print(type(b))

# Convertir de x a deimal
a = 3
b = float(a)
print(type(b))

# Convertir de x a String
a = 3
b = str(a)
print(type(b))

# Concatenaciones
a = 'hola'
b = 'mundo'
c = a + ' ' + b

a = 'hola'
b = a * 5
print(b)

# Capturar por pantalla
nombre = input('Digite su nombre: ')
print('Hola',nombre, sep='**', end='ROBERTO')


nombre = input('Digite su nombre: ')
print('Hola' + nombre)

# Interpolación

nombre = input('Digite su nombre: ')
print(f'Su nombre es {nombre}')


# HUA que sume dos numeros e impima su resultado

numero_uno = int(input('Digite el número uno: '))
numero_dos = int(input('Digite el número dos: '))
suma = numero_uno + numero_dos
print(f'El resultado de sumar {numero_uno} + {numero_dos} es: {suma}')



# HUA que lea un número y lo eleve al cuadrado

num = int(input("Ingresa número: "))
alcuadrado = num ** 2
print(f"{num} elevado al cuadrado es: {alcuadrado}")


# HUA que tome el valor de un producto, le aplique el 20%
# de descuento, imprima el valor del producto inicial,
# el valor con descuento y el valor ahorrado


p_value = int(input("Ingrese el valor del producto: $"))
descuento = p_value * 0.20
valor_final = p_value - descuento
print(f'El valor del producto inicial es de: ${p_value:,}')
print(f"El valor ahorrado es de: ${descuento:,}")
print(f"El valor con el descuento aplicado es de: ${valor_final:,}")


# Condicionales

# Tabla de verdad

# Tabla del and

print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) #False

# Tabla del or

print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) #False

# Negación

print(not True)
print(not False)

# Jerarquía de Operaciones
# 1. Paréntesis y llaves
# 2. Potencias y Raices
# 3. Multiplicación y División
# 4. Sumas y Restar


print(True and False and True or 
     False or True or True) #True


print(True and (False and True) 
      or False or (True or True))

# Estructura if
x = 6
if (x > 0):
    print('1')
else:
    print('2')
    print('3')

if x > 0:
    print('Mayor que cero')
elif x == 0:
    print('Es igual a cero')
else:
    print('entró aquí')

# HUA que dada la edad de una persona
# indique si es mayor o menor de edad

edad = int(input('Digite la edad de la persona: '))
if edad >= 18:
    print('Es mayor de edad')
else:
    print('Es menor de edad')




# HUA que indique si un estudiante aprobó o reprobó una
# asignatura teniendo en cuenta que aprueba con mínimo
# una calificación de 3.0 hasta 5.0

nota = float(input('Digite el nota de la asignatura: '))
if nota >= 3:
    print(f'Aprobó la asignatura con una nota de {nota}.')
else:
    print(f'Reprobó la asignatura con una nota de {nota}.')


# HUA que indique si un estudiante aprobó o reprobó una
# asignatura teniendo en cuenta que aprueba con mínimo
# una calificación de 3.0, validando que sea una nota válida

nota = float(input('Digite el nota de la asignatura: '))
if nota < 0 or nota > 5:
    print(f'No es una nota válida')
elif nota >= 3:
    print(f'Aprobó la asignatura con una nota de {nota}.')
else:
    print(f'Reprobó la asignatura con una nota de {nota}.')

# HUA que dado un número n diga si es negativo, positivo o
# cero.

n = int(input('Digite el valor de n :'))
if n > 0:
    print(f'{n} es positivo')
elif n < 0:
    print(f'{n} es negativo')
else:
    print(f'{n} es cero')

# Ciclos en python

# For

# Range 

# Iterador Flojo

for valor in range(4):
    print(valor)

for valor in range(1, 6):
    print(valor)
    
for valor in range(1, 100, 2):
    print(valor)

for i in range(1, 11):
    for j in range(1, 6):
        print(i,j)

# While

while True:
    print('Hola Mundo')

# HUA que de las n notas de un estudiante calcule el promedio
# académico final
notas = 0
numero_notas = int(input('Digite el número de notas del estudiante: '))
for i in range(1, numero_notas + 1):
    while True:
        nota = float(input(f'Digite la nota número {i}: '))
        if nota <5 and nota > 0:
            break
    notas = notas + nota
prom = notas /numero_notas
prom = round(prom, 2)
print(f'El promedio académico final de las {numero_notas} notas es: {prom} ')


# Tipos de Colecciones

# Listas o vectores
# Tipo de datos mutable y ordenado

a = [2, 3, 4]
b = [2, True, 'hola', 3.4]
c = [2, [True, False], ['Hola', 'Mundo'], [2.3, 3.4, 4.6, 7.8]]

for var in c:
    print (var)

a[0] = 7
print(b[2])

a = [2, 3, 4]
a.append(5)  # Agrega el elemento al final de la lista
a.remove(3)  # Elimina de la lista un elemento por su valor
a.pop()  # Elimina el último elemento del vector
a.pop(1)  # Elimina un elemento por posición
a.clear()  # Elimina todos los elementos del vector
# del a
4 in a  # Busca el elemento 4 dentro de a
len(a)  # Cantidad de elementos de la lista

b = a[:]

# Tuplas
# Tipo de datos inmutable y ordenado

a = (1, 2, 3, 4)
print(a[1])
a = (1, 'hola', True, 4.5)
a = (1, ['hola', 'Mundo'], True, 4.5)
a = (1, ['hola', 'Mundo'], (True, False), 4.5)
4 in a


# Set
# Mutables y NO ordenados
a = {1, 2, 3, 4}
a = {7, 2, 1, 5, 9, 9}

# Diccionario
# Mutable pero no ordenado

a = {'nombre': 'Roberto', 'apellido': 'Morales'}
a = {1: 'Roberto', 2: 'Morales'}

a['nombre']
a['nombre'] = 'Carlos'


for valor in a:
    print(valor)

for valor in a.values():
    print(valor)
    
for valor in a.keys():
    print(valor)

for valor in a.items():
    print(valor)
    
for llave, valor in a.items():
    print(f'Llave: {llave}, Valor: {valor}')


# Valores vación de un tipo de dato

a = [] # array
b = () # tupla
c = set() #set
d = {} # diccionario

# Un solo elemento

a = [1] #array
b = (3,) #tupla
c = {2} #Set

# Funciones

def saludar():
    print('Hola Mundo')
    
def saludar(nombre):
    print(f'Hola {nombre}')


# Parámetros opcionales

def saludar(nombre = 'Mundo'):
    print(f'Hola {nombre}')


def saludar(nombre, apellido = ""):
    print(f'Hola {nombre} {apellido}')


def saludar(nombre="Mundo", apellido = ""):
    print(f'Hola {nombre} {apellido}')

def saludar(nombre, apellido="", apellido_dos="", alias =""):
    print(f'Hola {nombre} {apellido}')
    
# Parámetros ilimitados

def saludar(*nombres):
    print(f'Hola {nombres}')
    
def saludar(*nombres):
    for nombre in nombres:
        print(nombre, end=' ')

print('Roberto', 'Carlos', 'Pedro')


def saludar(*nombre, apellido):
    print(nombre, apellido)
    
    
def saludar(*nombre, apellido =""):
    print(nombre, apellido)

def saludar(**nombres):
    print(nombres)

def saludar(*nombre, **nombres):
    print(nombre)
    print(nombres)

def sumar(num_uno = 5, num_dos =6):
    return num_uno + num_dos

def operaciones(num_uno = 5, num_dos =6):
    suma = num_uno + num_dos
    resta = num_uno - num_dos
    mult = num_uno * num_dos
    div = num_uno / num_dos
    return suma, resta, mult, div

_, _, multip, _ = operaciones()

def sumar:
    pass
