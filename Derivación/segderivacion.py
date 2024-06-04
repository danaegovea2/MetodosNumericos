import numpy as np
import matplotlib.pyplot as plt

def deriv2(f, a, b, n):
    x = np.linspace(a, b, n)
    dx = (b - a)/(n - 1)
    y = f(x)
    yp = np.zeros_like(x)
    ypp = np.zeroslike(x)
    # fórmulas de segunda derivada 
    for i in range(n):
        if i==0:
            ypp[i] = (y[i + 2] - 2 * y[i + 1] + y[i]) / dx**2 # derivada hacia adelante
        elif i== n - 1:
            ypp[i] = (y[i] - 2*y[i - 1] + y[i - 2])/dx**2 # derivada hacia atrás
        else:
            ypp[i]=(y[i + 1] - 2*y[i] + yp[i - 1])/ dx**2

plt.plot(x, ypp, 'g*')
plt.show()
