# chi cuadrada para polinomio grado 2 y grado 3
# para imprimir valores, escribir al final:
# 
# dataxs = np.array([34, 27, 65, 20, 53, 49, 42, 31, 55, 61])
# datays = np.array([4.5, 3, 7, 3.5, 8, 5, 4, 4, 5.5, 7.5])  <--- inroducir tus propios datos
# ajuste_polinomial(dataxs, datays)
import matplotlib.pyplot as plt
import numpy as np

def phi(n,k,x):
    if n==2:
        val = x**k
    elif n==3:
        val = x**k
    return val

def normalfit(dataxs,datays,datasigs,n):
    N = dataxs.size
    A = np.zeros((N,n))
    for k in range(n):
        A[:,k] = phi(n,k,dataxs)/datasigs
    bs = datays/datasigs
    matI = A.T@A
    InvmatI = np.linalg.inv(matI)
    matD = A.T@bs
    cs = InvmatI@matD
    
    sigS = np.diagonal(InvmatI)
    chisq = np.sum((bs - A@cs)**2)
    return cs, chisq, sigS, InvmatI


def plotresults(dataxs, datays, datasigs, cs, n):
    x = np.linspace(min(dataxs), max(dataxs), 1000)
    y = sum(c*x**i for i, c in enumerate(cs))

    plt.figure(figsize=(10,6))
    plt.errorbar(dataxs, datays, yerr=datasigs, fmt='o', label='Datos')
    plt.plot(x, y, label=f'Ajuste polinomial de grado {n}')
    plt.title(f'Resultados para n={n}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

def ajuste_polinomial(dataxs, datays):
    N = dataxs.size
    datasigs = 0.2 * np.abs(np.random.randn(N))
    
    csVal, sigVal, sigData = [], [], []
    
    for n in (2, 3):
        cs, chisq, sigS, sigD = normalfit(dataxs,datays,datasigs,n)
        csVal.append(cs)
        sigVal.append(np.sqrt(sigS))
        sigData.append(sigD) 
        print()
        print('El valor para chi^2 es ', chisq)
        print('El valor para chi^2 por grado de libertad es: ', chisq/(dataxs.size - cs.size))
        print('El valor de los parámetros c_i son ', cs)
        plotresults(dataxs, datays, datasigs, cs, n)
    return csVal, sigVal, sigData