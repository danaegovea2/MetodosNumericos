import numpy as np
def itera(f, p0, tol, n0):
    i = 0
    while (i <= n0):
      p = f(p0)
      if (abs(p - p0) < tol):
        return p
      i += 1
      p0 = p

e = input('¿Cuál es tu función? ')
f = lambda x: eval(e)
p0 = float(input('Dame tu aproximación inicial '))
tol = float(input('Dame la tolerancia '))
n0 = int(input('Dame el número máximo de iteraciones '))

print(itera(f, p0, tol, n0))
