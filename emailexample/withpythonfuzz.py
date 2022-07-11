from pythonfuzz.main import PythonFuzz

from emailexample.libmail import valid_email


@PythonFuzz
def fuzz(buf):
    try:
        email = buf.decode('utf-8')
    except UnicodeDecodeError:
        return
    valid_email(email)


if __name__ == '__main__':
    fuzz()
