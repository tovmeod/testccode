from hypothesis import given, settings
from hypothesis.strategies import integers

from pi3._pi import lib

# pytest pi3/tests.py::test_with_hypothesis


@given(integers())
def test_with_hypothesis(n):
    approx = lib.pi_approx(n)
    assert str(approx).startswith("3.")
"""
Falsifying example: test_with_hypothesis(
    n=2147483648,
)
n = 2147483648

    @given(integers())
    def test_with_hypothesis(n):
>       approx = lib.pi_approx(n)
E       OverflowError: integer 2147483648 does not fit '32-bit int'

"""


@given(integers(min_value=0, max_value=2147483647))
def test_with_hypothesis2(n):
    approx = lib.pi_approx(n)
    assert str(approx).startswith("3.")
# hypothesis.errors.Flaky: Hypothesis test_with_hypothesis2(n=0) produces unreliable results: Falsified on the first call but did not on a subsequent one
# I'm giving up after this, the code is bad, and you should feel bad
