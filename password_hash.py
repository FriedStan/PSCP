"""Password but hash"""
import hashlib


def let_hash(password):
    """Hash in SHA512"""
    hashed = hashlib.sha512(bytes(password, "UTF-8")).hexdigest()
    print(hashed.upper())


let_hash(str(input()))
