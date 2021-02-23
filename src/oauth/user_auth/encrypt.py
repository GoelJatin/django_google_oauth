import hashlib


def encrypt(salt, password):
    """Encodes the password using the given value of **salt** and
        the SHA512 algorithm.
    """
    if not isinstance(password, bytes):
        password = password.encode()

    return hashlib.sha512(password + salt).digest()
