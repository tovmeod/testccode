import sys

import atheris
import dns
from hypothesis import given
from hypothesis.strategies import ip_addresses

with atheris.instrument_imports():
    from dns.ipv4 import inet_ntoa, inet_aton


@atheris.instrument_func
def test_one_input(data):
    try:
        ip = inet_ntoa(data)
    except dns.exception.SyntaxError:
        return
    assert inet_aton(ip) == data


@given(ip_addresses(v=4))
def test_with_hypothesis(ip):
    ip = str(ip)
    ipbytes = inet_aton(ip)
    assert inet_ntoa(ipbytes) == ip


if __name__ == '__main__':
    atheris.Setup(sys.argv, test_one_input)  # slow
    atheris.Fuzz()

    # atheris.Setup(sys.argv, atheris.instrument_func(test_with_hypothesis.hypothesis.fuzz_one_input))
    # atheris.Fuzz()

# python dnsexample/withatheris.py -atheris_runs=100000 dnsexample/corpus -max_len=8
