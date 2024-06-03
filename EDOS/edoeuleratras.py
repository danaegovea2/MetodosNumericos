import matplotlib.pyplot as plt

def eulerbckw(f, a, b, y0, n): # a, b: límites del intervalo, f: función, y0: valor inicial de la función, n: número de pasos
    x2 = np.linspace(a, b, n+1) 
    y2 = np.zeros(n+1)
    y2[0]=y0
    h = (b - a)/n
    for i in range(1, n+1):
        xi = x2[i]
        yf = y2[i-1] + h * f(xi, y2[i-1])  # Utilizamos el método de Euler explícito para la estimación inicial
        y2[i] = y2[i-1] + h * f(xi, yf)   # Corregir usando la nueva estimación
    return(x2, y2)

x2, y2 = eulerbckw(f, a, b, y0, n)
# print(eulerbckw)
plt.plot(x2, y2)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Euler implícito')
plt.grid(True)
plt.show()