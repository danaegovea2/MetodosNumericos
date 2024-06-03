import numpy as np
import matplotlib.pyplot as plt

def eulerforw(x0, xf, y0, n, func):
    
    deltax = (xf-x0) / (n - 1) # cálculo de la delta
    x1 = np.linspace(x0, xf, n)
    y1 = np.zeros(n)
    
    y1[0] = y0 #almacenar
    for i in range(1, n):
        y1[i] = deltax * func(x1[i-1], y1[i-1]) + y1[i-1] # fórmula
    return x1, y1

# Definir los valores iniciales y parámetros
x0 = 0  # Valor inicial de x
xf = 1  # Valor final de x
y0 = 1  # Valor inicial de y
n = 100  # Número de puntos
func = lambda x, y: x * y  # Función a integrar
x1, y1 = eulerforw(x0, xf, y0, n, func)
# print(eulerforw)
plt.plot(x1, y1)
plt.xlabel('Valores de x')
plt.ylabel('Valor de y')
plt.title('Método de Euler hacia adelante')
plt.show()