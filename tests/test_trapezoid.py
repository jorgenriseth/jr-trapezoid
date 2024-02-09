import pytest

import jr_trapezoid as jrt


def test_trapezoid():
    assert jrt.trapezoid(lambda x: x, 0, 2, 10) == pytest.approx(2.0)


def test_numpy_trapezoid():
    assert jrt.numpy_trapezoid(lambda x: x, 0, 2, 10) == pytest.approx(2.0)
