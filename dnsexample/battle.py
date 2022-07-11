import dns
from battle_tested import fuzz

from dns.ipv4 import inet_ntoa, inet_aton

if __name__ == '__main__':
    fuzz(inet_ntoa, allow=(dns.exception.SyntaxError,))
