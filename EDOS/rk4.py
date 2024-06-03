import numpy as np
import matplotlib.pyplot as plt

def runge_kutta(x0, y0, xn, n, f): # x0, y0: intrvalo, xn: valor inicial, n: número de pasos, f: función
    h = (xn-x0)/float(n)
    x3 = np.linspace(x0, xn, n+1)
    y3 = np.zeros(n+1)
    y3[0] = y0
    for i in range(n):
        k1 = h * f(x3[i], y3[i])
        k2 = h * f(x3[i] + 0.5*h, y3[i] + 0.5*k1)
        k3 = h * f(x3[i] + 0.5*h, y3[i] + 0.5*k2)
        k4 = h * f(x3[i] + h, y3[i] + k3)
        y3[i+1] = y3[i] + (k1 + 2*k2 + 2*k3 + k4)/6
    return x3, y3

x3, y3 = runge_kutta(x0, y0, xn, n, f)
# print(runge_kutta)

# Gráfica
plt.plot(x3, y3, '*-')
plt.title('Runge-Kutta')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()