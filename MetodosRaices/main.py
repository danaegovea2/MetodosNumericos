!wget https://raw.githubusercontent.com/danaegovea2/MetodosNumericos/main/MetodosRaices/metodos_num.py
from metodos_num import *

import numpy as np
from scipy.misc import derivative

def menu():
  print('Escoge un método ')
  print('1. Bisección')
  print('2. Newton Raphson ')
  print('3. Punto fijo ')
  print('4. Método de la secante ')
  print('5. Método de la secante v2.')
  opcion = int(input('Opción: '))

  if opcion == 1:
    e = input('¿Cuál es tu función?')
    f = lambda x: eval(e)
    interv = input('Dame tu intervalo ')
    n0 = int(input('Dame el número máximo de iteraciones '))
    tol = float(input('Dame la tolerancia '))
    print(biseccion(f, interv, tol, n0))

  elif opcion == 2:
    e = input('¿Cuál es tu función? ')
    f = lambda x: eval(e)
    x0 = float(input('Dame la aproximación inicial: '))
    TOL = float(input('¿Cuál es tu tolerancia? '))
    n0 = int(input('Dame el número máximo de iteraciones que quieres: '))
    print(newton(f, x0, TOL, n0))

  elif opcion == 3:
    e = input('¿Cuál es tu función? ')
    f = lambda x: eval(e)
    p0 = float(input('Dame tu aproximación inicial '))
    tol = float(input('Dame la tolerancia '))
    n0 = int(input('Dame el número máximo de iteraciones '))
    print(itera(f, p0, tol, n0))

  elif opcion == 4:
    expresion = input("Ingrese la función f(x): ")
    funcion_ejemplo = lambda x: eval(expresion)
    x0 = float(input("Ingrese el valor inicial x0: "))
    x1 = float(input("Ingrese el valor inicial x1: "))
    tol = float(input("Ingrese la tolerancia: "))
    n0 = int(input("Ingrese el número máximo de iteraciones: "))
    raiz = secante(funcion_ejemplo, x0, x1, tol, n0)
    print("Aproximación de la raíz:", raiz)

  elif opcion == 5:
    e = input('¿Cuál es tu función? ')
    f = lambda x: eval(e)
    interv = input('Dame el intervalo ')
    tol = float(input('Dame la tolerancia '))
    n0 = int(input('Dame el número maximo de iteraciones '))
    print(secante2(f, interv, tol, n0))

menu()
