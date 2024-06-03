import numoy as np
import matplotlib.pyplot as plt

def deriv(f, a, b, n):
    x = np.linspace(a, b, n)
    dx = (b - a)/(n - 1)
    y = f(x)
    yp = np.zeros_like(x)
    for i in range(n):
        if i==0:
            yp[i] = (y[i + 1] - y[i]) / dx # derivada hacia adelante
        elif i== n - 1:
            yp[i] = (y[i] - y[i - 1])/dx # derivada hacia atrás
        else:
            yp[i]=(y[i + 1] - y[i - 1])/ (2*dx) # derivada central

plt.plot(x, yp, 'g*')
plt.show()