import sys

import atheris
from hypothesis import given
from hypothesis.strategies import emails

with atheris.instrument_imports():
    import libmail
    # from emailexample import libmail


@atheris.instrument_func
def test_one_input(data):
    libmail.valid_email(data)


@given(emails())
@atheris.instrument_func
def test_with_hypothesis(n):
    libmail.valid_email(n)


if __name__ == '__main__':
    # atheris.Setup(sys.argv, test_one_input)  # slow
    # atheris.Fuzz()

    atheris.Setup(sys.argv, atheris.instrument_func(test_with_hypothesis.hypothesis.fuzz_one_input))
    atheris.Fuzz()

# python emailexample/withatheris.py -atheris_runs=1000000 emailexample/corpus -max_len=8