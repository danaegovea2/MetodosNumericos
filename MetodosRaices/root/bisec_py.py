import numpy as np
def biseccion(f, interv, tol, n0):
  a, b = map(float, interv.split(','))
  i = 1
  while (i <= n0):
    p = a + (b - a)/2
    if (abs(b - a) < tol):
      return p
    if (f(p)*f(a) > 0):
      a = p
    else:
      b = p
    i =+ 1


e = input('¿Cuál es tu función? ')
f = lambda x: eval(e)
interv = input('Dame tu intervalo ')
n0 = int(input('Dame el número máximo de iteraciones '))
tol = float(input('Dame la tolerancia '))

print(biseccion(f, interv, tol, n0))
