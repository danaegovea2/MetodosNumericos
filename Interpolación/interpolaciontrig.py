# Interpolación trigonométrica donde se pide la función y los odos, a partir de ahí se consigue datays y dataxs, x = 0.3, en un intervalo de 
# 0 a pi/2 
import numpy as np
import matplotlib.pyplot as plt

def computeparams(dataxs, datays):
    n = dataxs.size
    m = (n + 1) // 2 if n % 2 == 0 else n // 2 + 1 # adaptación para casos pares e impares 
    ak = np.zeros(m)  # Inicialización de los coeficientes ak
    bk = np.zeros(m - 1)  # Inicialización de los coeficientes bk
    
    for k in range(m):
        ak[k] = np.dot(datays, np.cos(k * dataxs)) / n
    for k in range(1, m -1):
        bk[k] = np.dot(datays, np.sin(k * dataxs)) / n
    
    return ak, bk

def triginterp(aparams, bparams, x):
    n = aparams.size + bparams.size
    m = n // 2
    val = 0.5 * aparams[0]  # Término constante a0
    if n % 2 == 0:  # Caso par
        val += 0.5 * aparams[-1] * np.cos(m * x)  # Término de más alto grado am / 2
        for k in range(1, m):  # Términos de coseno
            val += aparams[k] * np.cos(k * x)
            val += bparams[k - 1] * np.sin(k * x)
            
    else:  # Caso impar
        for k in range(1, m + 1):  # Términos de coseno
            val += aparams[k] * np.cos(k * x)
            val += bparams[k - 1] * np.sin(k * x)

    return val

def generatedata(n, f, nodes="cheb", int=[-1, 1], endpoint=True):
    if nodes=="cheb": # NODOS
        dataxs = -np.cos(np.linspace(0, np.pi, n)) # fórmula para generar los nodos de chebyshev
    else:
        dataxs = np.linspace(int[0], int[1], n, endpoint=endpoint) # si no, generar nodos equiespaciados 
        datays = f(dataxs) # evaluar estos nodos en f para obtener los valores de datays
    return dataxs, datays

# ejemplo

funcion = input('función: ')
func = lambda x: eval(funcion)
n = input('nodos: ') # nodos 
dataxs, datays = generatedata(n, func, nodes=" ", int=[0, 0.5*np.pi], endpoint=False) ## datos, donde se encuentra el intervalo pedido
aparams, bparams = computeparams(dataxs, datays)
x = 0.3
pofx = triginterp(aparams, bparams, x)
print(x, func(x))
print(pofx)

# Gráfica
x = np.linspace(0, 2*np.pi, 100)
fig = plt.figure(figsize = (5,4))
plt.plot(x, func(x), 'k--')
daty = [triginterp(aparams, bparams, i) for i in x]
    
plt.plot(dataxs, datays, 'ro', label='Datos')
plt.plot(x, daty, c='r', label='Interpolada')
plt.plot(x, func(x), c='k', ls='-', lw=1, label='Analítica')
plt.legend(frameon=False)