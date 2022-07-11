from dns.ipv4 import inet_ntoa, inet_aton
from hypothesis import given
from hypothesis.strategies import ip_addresses


@given(ip_addresses(v=4))
def test_case_1_variant(ip):
    ip = str(ip)
    ipbytes = inet_aton(ip)
    assert inet_ntoa(ipbytes) == ip
