from typing import Callable

import dolfin as df
import numpy as np


def trapezoid(f: Callable[[float], float], a: float, b: float, N: int) -> float:
    dx = (b - a) / N
    integral = 0.0
    for i in range(N + 1):
        xi = a + i * dx
        integral += dx * f(xi)
    integral -= 0.5 * dx * (f(a) + f(b))
    return integral


def numpy_trapezoid(
    f: Callable[[np.ndarray], np.ndarray],
    a: float,
    b: float,
    N: int,
) -> float:
    x = np.linspace(a, b, N + 1)
    y = f(x)
    return ((b - a) / N) * (y.sum() - 0.5 * (y[0] + y[-1]))


def dolfin_trapezoid(
    f: Callable[[float], float],
    a: float,
    b: float,
    N: int,
) -> float:
    domain = df.IntervalMesh(N, a, b)
    fh = PyFunctionWrapper(f, degree=1)
    dx = df.Measure("dx", domain)
    return df.assemble(fh * dx)


class PyFunctionWrapper(df.UserExpression):
    def __init__(self, f: Callable[[float], float], **kwargs):
        super().__init__(self, **kwargs)
        self._f = f

    def eval(self, value, x):
        value[0] = self._f(float(x))

    def value_shape(self):
        return ()
