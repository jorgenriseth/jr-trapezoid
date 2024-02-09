from typing import Any, Callable

import numpy as np
from nptyping import NDArray, Shape


def trapezoid(f: Callable[[float], float], a: float, b: float, N: int) -> float:
    dx = (b - a) / N
    integral = 0.0
    for i in range(N + 1):
        xi = a + i * dx
        integral += dx * f(xi)
    integral -= 0.5 * dx * (f(a) + f(b))
    return integral


def numpy_trapezoid(
    f: Callable[[NDArray[Shape["*"], float]], NDArray[Shape["*", float]]],
    a: float,
    b: float,
    N: int,
) -> float:
    x = np.linspace(a, b, N + 1)
    y = f(x)
    return ((b - a) / N) * (y.sum() - 0.5 * (y[0] + y[-1]))