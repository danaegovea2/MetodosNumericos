import numpy as np

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

# Entrada de usuario
expresion = input("Ingrese la función f(x): ")
funcion_ejemplo = lambda x: eval(expresion)

x0 = float(input("Ingrese el valor inicial x0: "))
x1 = float(input("Ingrese el valor inicial x1: "))
tol = float(input("Ingrese la tolerancia: "))
max_iter = int(input("Ingrese el número máximo de iteraciones: "))

# Método de la secante
raiz = secante(funcion_ejemplo, x0, x1, tol, max_iter)
print("Aproximación de la raíz:", raiz)
