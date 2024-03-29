def secante2(f, interv, tol, n0):
  a, b = map(float, interv.split(','))
  i=2
  if (f(a) > 0):
    p0 = b
    q0 = f(a)
    q1 = f(b)
  else:
    p0 = a
    q0 = f(b)
    q1 = f(a)
  while(i<=n0):
    if(f(a) > 0):
      p = p0 - (q1 / (q1 - q0)) * (p0 -a)
    else:
      p = p0 - (q1 / (q0 - q1)) * (b - p0)
    if (abs(p - p0) < tol):
      return p
    p0 = p
    q1 = f(p)
    i += 1
    return p

#Entrar datos
e = input('¿Cuál es tu función? ')
f = lambda x: eval(e)
interv = input('Dame el intervalo ')
tol = float(input('Dame la tolerancia '))
n0 = int(input('Dame el número maximo de iteraciones '))

print(secante2(f, interv, tol, n0))
