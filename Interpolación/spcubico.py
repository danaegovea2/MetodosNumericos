#puntos
import numpy as np
import matplotlib.pyplot as plt

f = input('función: ')
func = lambda x: eval(f)
#1 / (1 + 25*x**2
x = np.linspace(-1, -0.2, 30) # se crea un arreglo con 15 puntos equidistantes de -1, 1
y = func(x)
dataxs, datays = x, y

def computecs(dataxs, datays):
    n = len(dataxs)
    A = np.zeros((n-2,n-2))
    np.fill_diagonal(A, 2*(dataxs[2:]-dataxs[:-2]))
    np.fill_diagonal(A[1:,:], dataxs[2:-1]-dataxs[1:-2])
    np.fill_diagonal(A[:,1:], dataxs[2:-1]-dataxs[1:-2])
    b1 = (datays[2:]-datays[1:-1])/(dataxs[2:]-dataxs[1:-1])
    b2 = (datays[1:-1]-datays[:-2])/(dataxs[1:-1]-dataxs[:-2])
    bs = 6*(b1 - b2)

    cs = np.zeros(n)
    cs[1:-1] = np.linalg.solve(A, bs)
    return cs

def splineinterp(dataxs,datays,cs,x):
    k = np.argmax(dataxs>x)
    xk = dataxs[k]; xk1 = dataxs[k-1]
    yk = datays[k]; yk1 = datays[k-1]
    ck = cs[k]; ck1 = cs[k-1]

    val = yk1*(xk-x)/(xk-xk1) + yk*(x-xk1)/(xk-xk1)
    val -= ck1*((xk-x)*(xk-xk1) - (xk-x)**3/(xk-xk1))/6
    val -= ck*((x-xk1)*(xk-xk1) - (x-xk1)**3/(xk-xk1))/6
    return val

cs = computecs(dataxs, datays)
x_val = 0.95
pofx = splineinterp(dataxs, datays, cs, x)
print(x, pofx, func(x))

#gráfica
plt.plot(x, y, '*r', label = 'Datos originales')
plt.legend()
plt.show()