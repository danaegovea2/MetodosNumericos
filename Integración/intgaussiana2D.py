import numpy as np

funcion = input('Dame la funcion: ')
f = lambda x, y: eval(funcion)
interv_x = [float(input('Dame el límite inferior en x: ')), float(input('Dame el límite superior en x: '))]
interv_y = [float(input('Dame el límite inferior en y: ')), float(input('Dame el límite superior en y: '))]
n = 4

# Función de Legendre para dos variables
def legendre_2d(n, x, y):
    valn_x, dvaln_x = legendre(n, x)
    valn_y, dvaln_y = legendre(n, y)
    return valn_x * valn_y, dvaln_x * valn_y, valn_x * dvaln_y

# Adaptación de legroots para dos dimensiones
def legroots_2d(n, delta=0.2, itera=1700, err='dist', err2=5e-05):
    roots = np.zeros((n, n))
    npos = n // 2
    f = lambda x, y: legendre_2d(n, x, y)[0]
    for i in range(npos):
        p0 = np.cos(np.pi * (4 * i + 3) / (4 * n + 2))
        for j in range(npos):
            q0 = np.cos(np.pi * (4 * j + 3) / (4 * n + 2))
            root_x = secante(lambda x: f(x, q0), p0, p0 + delta, tol=err2, max_iter=itera)
            root_y = secante(lambda y: f(root_x, y), q0, q0 + delta, tol=err2, max_iter=itera)
            roots[i, j] = -root_y
            roots[-1 - i, -1 - j] = root_y
            roots[i, -1 - j] = -root_y
            roots[-1 - i, j] = root_y
    return roots

# Adaptación de paramgauss para dos dimensiones
def paramgauss_2d(n, delta=0.2, itera=1700, err='dist', err2=5e-05):
    xroot, w_x = paramgauss(n, delta=delta, itera=itera, err=err, err2=err2)
    yroot, w_y = paramgauss(n, delta=delta, itera=itera, err=err, err2=err2)
    return xroot, yroot, w_x, w_y

# Adaptación de gaussint para dos dimensiones
def gaussint_2d(f, interv_x, interv_y, n, delta=0.2, itera=1700, err='dist', err2=5e-05):
    xs, ys, ws_x, ws_y = paramgauss_2d(n, delta=delta, itera=itera, err=err, err2=err2)
    ta_x = 0.5 * (interv_x[1] + interv_x[0])
    tb_x = 0.5 * (interv_x[1] - interv_x[0])
    ta_y = 0.5 * (interv_y[1] + interv_y[0])
    tb_y = 0.5 * (interv_y[1] - interv_y[0])

    t_x, t_y = np.meshgrid(ta_x + tb_x * xs, ta_y + tb_y * ys)
    fk = ws_x[:, np.newaxis] * ws_y[np.newaxis, :] * f(t_x, t_y)
    val = tb_x * tb_y * np.sum(np.sum(fk, axis=0), axis=0)
    return val

# Imprimir resultados
interv_x = [0., 1.]
interv_y = [0., 1.]
val = gaussint_2d(f, interv_x, interv_y, n)
print('El resultado de la integración doble es', val)