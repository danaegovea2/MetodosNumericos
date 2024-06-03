import numpy as np
import matplotlib.pyplot as plt

def funcionesSAbrev(Sx, Sy, Sxx, Sxy, N):
    Sf = N
    Sxf = Sx
    Syf = Sy
    Sxxf = Sxx
    Sxyf = Sxy
    Triangf = Sf * Sxxf - Sxf**2
    return Sf, Sxf, Syf, Sxxf, Sxyf, Triangf

def computecs(Sx, Sy, Sxx, Sxy, N):
    Sf, Sxf, Syf, Sxxf, Sxyf, Triangf = funcionesSAbrev(Sx, Sy, Sxx, Sxy, N)
    
    cs = np.zeros(2)  # Coeficientes de mejor ajuste
    sigcs = ([2.5, 3])  # Desviaciones estándar
    
    cs[0] = (Sxxf * Syf - Sxf * Sxyf) / Triangf
    cs[1] = (Sf * Sxyf - Sxf * Syf) / Triangf
    sigcs[0] = np.sqrt(Sxxf / Triangf)
    sigcs[1] = np.sqrt(Sf / Triangf)
    return cs, sigcs

datasigs = 3 * np.abs(np.random.randn(N))

# Calcular coeficientes
# ESCRIBIR ESTOS DATOS EN LA NOTEBOOK DE DONDE SE LLAMA 
# cs, sigcs = computecs(Sx, Sy, Sxx, Sxy, N)

print(f'Coeficientes: c0={cs[0]}, c1={cs[1]}')

# Graficar resultados 
x = np.linspace(0, 50, 100)
y = cs[0] + cs[1] * x

plt.figure(figsize=(10, 6))
plt.plot(x, y, color = 'purple', label=f'y = {cs[0]:.2f} + {cs[1]:.2f}x')
plt.title('Ajuste lineal usando sumas abreviadas y medias')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()