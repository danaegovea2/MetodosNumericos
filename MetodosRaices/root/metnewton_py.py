from scipy.misc import derivative
#derivative(f,x0) <- derivada de la función en un punto x0

def newton(f, x0, TOL, n0):
    i = 1

    while i <= n0:
        xn = x0 - f(x0) / derivative(f,x0)

        if (abs(f(xn) - f(x0)) < TOL):
            print('La raíz aproximada es:', xn)
            return xn
        if (i == n0):
          print('El método falló después de ', n0,' iteraciones')

        x0 = xn
        i += 1

e = input('¿Cuál es tu función? ')
f = lambda x: eval(e)
x0 = float(input('Dame la aproximación inicial: '))
TOL = float(input('¿Cuál es tu tolerancia? '))
n0 = int(input('Dame el número máximo de iteraciones que quieres: '))

print(newton(f, x0, TOL, n0))
