import numpy as np
from scipy.misc import derivative

def biseccion(f, interv, tol, n0):
  a, b = interv.split(',')
  i = 1
  while (i <= n0):
    p = (a + b)/2
    if (abs(b - a) < tol):
      return p
    if (f(p)*f(a) > 0):
      a = p
    else:
      b = p
    i =+ 1


def newton(f, x0, TOL, n0):
    i = 1

    while i <= n0:
      xn = x0 - f(x0) / derivative(f,x0)

      if (abs(f(xn) - f(x0)) < TOL):
          print('La raíz aproximada es:', xn)
          return xn
      if (i == n0):
        print('El método falló después de ', n0,' iteraciones')

      x0 = xn
      i += 1

def itera(f, p0, tol, n0):
    i = 0
    while (i <= n0):
      p = f(p0)
      if (abs(p - p0) < tol):
        return p
      i += 1
      p0 = p


def secante(f, x0, x1, tol, max_iter):
    i = 0
    while i < max_iter:
        x2 = x1 - f(x1) * ((x1 - x0) / (f(x1) - f(x0)))
        if abs(x2 - x1) < tol:
            return x2
        x0 = x1
        x1 = x2
        i += 1
    raise ValueError("El método no converge después de {} iteraciones.".format(max_iter))


def secante2(f, interv, tol, n0):
  a, b = interv.split(',')
  a = float(a)
  b = float(b)
  i=2
  if (float(f(a)) >= 0):
    p0 = float(b)
    q0 = float(f(a))
    q1 = float(f(b))
  else:
    p0 = float(a)
    q0 = float(f(b))
    q1 = float(f(a))
  while(i<=n0):
    if(float(f(a)) > 0):
      p = p0 - (q1 / (q1 - q0)) * (p0 -a)
    else:
      p = p0 - (q1 / (q0 - q1)) * (b - p0)
    if (abs(p - p0) < tol):
      return p
    p0 = p
    q1 = float(f(p))
    i += 1
    return p
