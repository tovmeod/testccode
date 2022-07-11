from hypothesis import given, settings
from hypothesis.strategies import integers

from pi2._pi import lib

# pytest pi2/tests.py::test_with_hypothesis


@given(integers())
def test_with_hypothesis(n):
    approx = lib.pi_approx(n)
    assert str(approx).startswith("3.")
# this takes too long, gave up after 215.33s (0:03:35)


@settings(deadline=0.1)  # for each test case, in ms, still too long
@given(integers())
def test_with_hypothesis2(n):
    approx = lib.pi_approx(n)
    assert str(approx).startswith("3.")
