from math import isnan

from hypothesis import given, assume
from hypothesis.strategies import integers
from pi._pi import lib


def test_approx():
    approx = lib.pi_approx(10)
    assert str(approx).startswith("3.")

    approx = lib.pi_approx(10000)  # 100k
    assert str(approx).startswith("3.1")


@given(integers())
def test_with_hypothesis(n):
    approx = lib.pi_approx(n)
    assert str(approx).startswith("3.")
# pycharm does not show enough information
# pytest pi/tests.py::test_with_hypothesis


@given(integers())
def test_with_hypothesis2(n):
    assume(not isnan(n))
    approx = lib.pi_approx(n)
    assert str(approx).startswith("3.")


@given(integers())
def test_with_hypothesis3(n):
    assume(not isnan(n))
    assume(n != 0)
    approx = lib.pi_approx(n)
    assert str(approx).startswith("3.")


@given(integers())
def test_with_hypothesis4(n):
    assume(not isnan(n))
    assume(n != 0)
    assume(n != 1)
    approx = lib.pi_approx(n)
    assert str(approx).startswith("3.")


@given(integers())
def test_with_hypothesis5(n):
    assume(not isnan(n))
    assume(n > 1)
    approx = lib.pi_approx(n)
    assert str(approx).startswith("3.")

# Flaky example! Hypothesis test_with_hypothesis5(n=126) produces unreliable results: Falsified on the first call but did not on a subsequent one


@given(integers(min_value=2))
def test_with_hypothesis6(n):
    approx = lib.pi_approx(n)
    assert str(approx).startswith("3.")

"""
E       AssertionError: assert False
E        +  where False = <built-in method startswith of str object at 0x7f9fdfb991f0>('3.')
E        +    where <built-in method startswith of str object at 0x7f9fdfb991f0> = '4.0'.startswith
E        +      where '4.0' = str(4.0)

pi/tests.py:63: AssertionError
-------------------------------------------------------------------------------------------------------------- Hypothesis --------------------------------------------------------------------------------------------------------------
Falsifying example: test_with_hypothesis6(
    n=2,
)
"""

# @settings(deadline=500)
@given(integers(min_value=-2147483647, max_value=2147483647))
# @given(integers())
def test2_with_hypothesis(n):
    assume(not isnan(n))
    # assume(-2147483647 <= n <= 2147483647)
    assume(n != 0)
    assume(n != 1)
    approx = lib.pi_approx(n)
    assert str(approx).startswith("3.")
