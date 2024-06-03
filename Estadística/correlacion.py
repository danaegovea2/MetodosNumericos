# se calcula el coeficiente de pearson con una función de scipy
# dataxs = np.array([34, 27, 65, 20, 53, 49, 42, 31, 55, 61])
# datays = np.array([4.5, 3, 7, 3.5, 8, 5, 4, 4, 5.5, 7.5])  <---- reescribir datos 
# se utiliza from scipy.stats import pearsonr
# Calcular el coeficiente de correlación de Pearson
# El coeficiente de correlación lineal de Pearson indica que si r = 0 entonces no hay correlación entre los datos dados.
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

def calcular_correlacion(dataxs, datays):
    coefc, _ = pearsonr(dataxs, datays)
    
    umbral = 0.1

    if abs(coefc) < umbral:
        print(f"El coeficiente de correlación de Pearson r={coefc:.3f} es cercano a cero.")
    else:
        print(f"El coeficiente de correlación de Pearson r={coefc:.3f} no es cercano a cero.")
    
    # Crear la gráfica de dispersión
    plt.scatter(dataxs, datays, color='blue', label='Datos')
    plt.title('Correlación de los Datos')
    plt.xlabel('dataxs')
    plt.ylabel('datays')
    
    # Añadir una línea de regresión
    slope, intercept = np.polyfit(dataxs, datays, 1)
    plt.plot(dataxs, slope * dataxs + intercept, color='red', label='Línea de Regresión')
    plt.legend()
    plt.grid(True)
    plt.show()