import pytest

import jr_trapezoid as jrt


def test_trapezoid():
    assert jrt.trapezoid(lambda x: x, 0, 2, 10) == pytest.approx(2.0)


def test_numpy_trapezoid():
    assert jrt.numpy_trapezoid(lambda x: x, 0, 2, 10) == pytest.approx(2.0)


def test_dolfin_trapezoid():
    assert jrt.dolfin_trapezoid(lambda x: x, 0, 2, 10) == pytest.approx(2.0)
    assert jrt.dolfin_trapezoid(lambda x: x**2, 0, 1, 1) == pytest.approx(0.5)
