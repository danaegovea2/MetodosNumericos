import matplotlib.pyplot as plt
import numpy as np

# Definir las constantes
q = 1.0  # Carga de cada una de las cargas puntuales
d = 0.1  # Distancia entre las cargas puntuales

# Función para calcular el campo eléctrico en un punto
def campo_electrico(x, y):
    r1 = np.sqrt((x - d/2)**2 + y**2)
    r2 = np.sqrt((x + d/2)**2 + y**2)
    E_x = (q / (4 * np.pi * r1**3)) * (x - d/2) - (q / (4 * np.pi * r2**3)) * (x + d/2)
    E_y = (q / (4 * np.pi * r1**3)) * y - (q / (4 * np.pi * r2**3)) * y
    return E_x, E_y

# Crear una malla de puntos
x, y = np.meshgrid(np.linspace(-1.5, 1.5, 500), np.linspace(-1.5, 1.5, 500))  # Usar np.meshgrid para crear la malla correctamente

# Calcular el campo eléctrico en cada punto de la malla
E_x, E_y = campo_electrico(x, y)

# Graficar las líneas de campo eléctrico
plt.streamplot(x, y, E_x, E_y, color='black', linewidth=0.5)

# Agregar las cargas puntuales
plt.scatter([-d/2, d/2], [0, 0], color='red', marker='o', s=50)

# Mostrar el gráfico
plt.show()
