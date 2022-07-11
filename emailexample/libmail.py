import re


def valid_email(email):
    return re.match(r'\w+@\w+\.\w+', email)
    # return re.match(br'\w+@\w+\.\w+', email)
    # return re.match(r'[\w/\-+]+@\w+\.\w+', email)
