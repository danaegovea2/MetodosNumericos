import numpy as npp
import matplotlib.pyplot as plt

funcion = input('función: ')
func = lambda x: eval(funcion)
dataxs = np.linspace(-1, 1, 30) # se crea un arreglo con 15 puntos equidistantes de -1, 1
datays = func(dataxs) # evaluar la función
L = 1 # para los coeficientes de lagrange
x = 0.3 # punto de interpolación

def lagrange(dataxs, datays, L, x):
    val = 0
    n = len(dataxs)
    for k in range(n): 
        L = 1
        for j in range(n):
            if j == k:
                continue
            L *= (x - dataxs[j]) / (dataxs[k] - dataxs[j]) # puntos cardinales de Lagrange
        val += datays[k] * L # fórmula de interpolación
    return val

y_interp = lagrange(dataxs, datays, L, x)

plt.plot(dataxs, datays, 'b', label='Datos originales')
plt.plot(x, y_interp, 'ro', label='Punto interpolado')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Interpolación de Lagrange')
plt.legend()
plt.grid(True)
plt.show()

print(x) # valor de la interpolación
print(func(x)) #función evaluada
print(y_interp) # Valor interpolado en el punto