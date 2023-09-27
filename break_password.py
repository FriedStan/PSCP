"""BreakPassword"""
import hashlib


def let_dehash(hashed):
    """Dehash in SHA512"""
    for i in iter(range(100000)):
        crack = hashlib.sha512(bytes("{:05d}".format(i), "UTF-8")).hexdigest().upper()
        if crack == hashed:
            print("{:05d}".format(i))
            break


let_dehash(str(input()))
