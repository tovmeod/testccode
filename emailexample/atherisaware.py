# Structure-aware Fuzzing
import sys

import atheris

with atheris.instrument_imports():
    import libmail


@atheris.instrument_func
def check_one_input(data):
    if len(data) >= 5:
        assert libmail.valid_email(data.decode('utf8'))


def split(string):
    chunk_size = len(string) / 3
    return string[0: 0 + chunk_size], string[1: 1 + chunk_size], string[2: 2 + chunk_size]


def custom_mutator(data, max_size, seed):
    try:
        a, b, c = split(data)
        decompressed = b'%s@%s.%s' % (a, b, c)
        if len(decompressed) > max_size:
            decompressed = decompressed[:max_size]
    except TypeError:
        decompressed = b'a@example.com'
        if len(decompressed) > max_size:
            decompressed = decompressed[:max_size]
    else:
        decompressed = atheris.Mutate(decompressed, len(decompressed))
    return decompressed


if __name__ == '__main__':
    atheris.Setup(sys.argv, check_one_input, custom_mutator=custom_mutator)
    atheris.Fuzz()

# python emailexample/atherisaware.py -atheris_runs=1000000 emailexample/corpus2 -max_len=20
