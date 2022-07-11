from battle_tested import fuzz

from emailexample.libmail import valid_email

if __name__ == '__main__':
    print(fuzz(valid_email))
