# Este programa acepta la EDO ya escrita de manera que el orden está reducido, en sistema se agrega el sistema 
# de ecuaciones que queda de haber reducido el orden de la EDO, después realiza la integración con el método de Runge-Kutta
# aplicado a este caso.

# Ya cuenta con valores iniciales, paso de integración y el punto final de la integración. Pueden ser modificados.
import numpy as np
import matplotlib.pyplot as plt

def sistema(x, Y):
    y, z = Y
    dydx = z
    dzdx = -0.25 * z
    return np.array([dydx, dzdx])

def ivp_rk4(f, x0, y0, z0, h, x_end):
    x_values = [x0]
    y_values = [y0]
    z_values = [z0]
    
    while x_values[-1] < x_end:
        x = x_values[-1]
        y = y_values[-1]
        z = z_values[-1]
        
        k1 = h * f(x, [y, z])
        k2 = h * f(x + 0.5 * h, [y + 0.5 * k1[0], z + 0.5 * k1[1]])
        k3 = h * f(x + 0.5 * h, [y + 0.5 * k2[0], z + 0.5 * k2[1]])
        k4 = h * f(x + h, [y + k3[0], z + k3[1]])
        
        y_new = y + (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6  # Usando los valores de k1, k2, k3, k4, se calcula un promedio ponderado
        z_new = z + (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6  # de las tasas de cambio para obtener un nuevo valor de y y z en el
                                                                 # siguiente punto.
        x_values.append(x + h)   # agregar los nuevos valores a cada lista (de x, y y z) para registrar
        y_values.append(y_new)   # la trayectoria de la solución durante la integración
        z_values.append(z_new)
    
    return x_values, y_values
