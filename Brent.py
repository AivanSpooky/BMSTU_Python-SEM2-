from scipy import optimize
from math import *

# Метод Брента (метод уточнения корня)
def brent(a, b, eps, nmax, f):
    try:
        root = optimize.root_scalar(f, method="brenth", bracket=(a, b), xtol=eps, maxiter=nmax)
        if (root.iterations < 0):
            raise Exception
    except Exception:
        return [f"[{a}; {b}]", "f(x0)*f(x1)>=0", "error", "error", 1]
    
    # Если значения близки к нулю - приравниваем к 0
    a = 0 if abs(a)<(abs(a-b)/2) else a
    b = 0 if abs(b)<(abs(a-b)/2) else b
    root.root = 0 if abs(root.root)<(abs(a-b)/2) else root.root
    
    return [f"[{a:.6g}; {b:.6g}]", f"{root.root:.6g}", f"{f(root.root):.1g}", root.iterations, 0]
