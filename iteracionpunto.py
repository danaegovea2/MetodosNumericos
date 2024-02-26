import numpy as np

def itera():
    func = lambda x: np.cos(x) - x
    gx = lambda x: np.cos(x)
    a = 0.5
    b = np.pi/2
    TOL = 0.01
    n0 = 20

    i = 1
    b = gx(a)
    p = abs(b - a)
    while not(p<=TOL or i>=n0):
        a = b
        b = gx(a)
        p = abs(b - a)
        i = i + 1
        res = b

    print(res)
    print(p)
    print(i)
       