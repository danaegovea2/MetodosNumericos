import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols
from sympy import lambdify
from sympy import sympify

def biseccion():
    x = symbols('x')
    fn = sympify(input('Ingresa la función'))
    f = lambdify(x, fn)

    a = float(input('Dame el valor inicial a: '))
    b = float(input('Dame el valor inicial b: '))
    N_0 = float(input('Ingrese el número máximo de iteraciones: '))
    i = 0
    TOL = 1
    x_pasada = 0

#Checar si se puede hacer el método de bisección
if f(a) * f(b) < 0:
    while TOL > N_0:
        p = (a + b)/2
        TOL = ((p - x_pasada) / p)

        if f(p) * f(a) > 0:
            b = p
        else:
            a = p
            x_pasada = p
            
    i = i + 1

    print('El valor de x es ', round(p, 9), 'con un error de ', round(TOL * 100, 9), "%")

else:
    print('La función no tiene una raíz en el intervalo de '+'x = '+ str(a) +' a x = '+ str(b)) #convertir las variables a string para evitar problemas
    print('Ingresa otros valores iniciales')