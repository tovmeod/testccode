from hypothesis import given
from hypothesis.strategies import emails

from emailexample.libmail import valid_email


def test_valid_email():
    assert valid_email('name@example.com')
    assert not valid_email('www.example.com')


@given(emails())
def test_with_hypothesis(n):
    assert valid_email(n)

# pytest .\emailexample\tests.py::test_with_hypothesis
# hypothesis write emailexample.libmail > .\emailexample\test_ghostwrited.py
