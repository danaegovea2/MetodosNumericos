# Usando los polinoomios de Legendre

import numpy as np

funcion = input('Dame la funcion: ')
f = lambda x: eval(funcion)
a = float(input('Dame el límite inferior: '))
b = float(input('Dame el límite superior: '))
n = 4

# Polinomios de Legendre
def bonnet(n, x):
    val0, val1 = 1, x
    for j in range(1, n):
        val2 = ((2 * j + 1) * x * val1 - j * val0) / (j + 1.)
        val0, val1 = val1, val2
    return val0, val1

def legendre(n, x):
    if n == 0:
        valn = 1. if isinstance(x, (int, float)) else [1.] * len(x)
        dvaln = 0. if isinstance(x, (int, float)) else [0.] * len(x)
    elif n == 1:
        valn = x
        dvaln = 1. if isinstance(x, (int, float)) else [1.] * len(x)
    else:
        valn_m1, valn = bonnet(n, x)
        dvaln = n * (valn_m1 - x * valn) / (1. - x**2)
    return valn, dvaln

# Método de la secante para raíces
def secante(f, x0, x1, tol, max_iter):
    i = 0
    while i < max_iter:
        x2 = x1 - f(x1) * ((x1 - x0) / (f(x1) - f(x0)))
        if abs(x2 - x1) < tol:
            return x2
        x0 = x1
        x1 = x2
        i += 1
    return x2

# Calcular raíces
def legroots(n, delta=0.2, itera=1700, err='dist', err2=5e-05):
    roots = np.zeros(n)
    npos = n // 2 #número de raíces positivas
    f = lambda x: legendre(n, x)[0]
    for i in range(npos):
        p0 = np.cos(np.pi * (4 * i + 3) / (4 * n + 2)) #semilla
        p1 = p0 + delta
        root = secante(f, p0, p1, tol=err2, max_iter=itera)
        roots[i] = -root
        roots[-1 - i] = root #acomodar y almacenar raíces positivas
    return roots

# Pesos y nodos (parámetros)
def paramgauss(n, delta=0.2, itera=1700, err='dist', err2=5e-05):
    xroot = legroots(n, delta=delta, itera=itera, err=err, err2=err2) #nodos para la cuadratura
    dPn = legendre(n, xroot)[1] #polinomio evaluado en el nodo y la derivada
    w = 2.0 / ((1.0 - xroot**2) * (dPn**2)) #calculo de los pesos
    return xroot, w

# Calcular la integral
def gaussint(f, interv, npts, delta=0.2, itera=1700, err='dist', err2=5e-05):
    xs, ws = paramgauss(npts, delta=delta, itera=itera, err=err, err2=err2)
    ta = 0.5 * (b + a) #regresar los intervalos
    tb = 0.5 * (b - a)
    t = ta + tb * xs #reescalar variables
    fk = ws * f(t) #evaluar la función y multiplicar por los pesos correspondientes
    val = tb * np.sum(fk) #suma de los valores de la función por los pesos
    return val

# Imprimir resultados
interv = [0., 1.]
val = gaussint(f, interv, n)
print('El resultado es', val)