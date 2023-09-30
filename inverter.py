"""Inverter"""


def inverter(bit):
    """Invert the binary"""
    invert = {"0": "1", "1": "0"}
    inverted = int("".join(iter(invert.get(i) for i in bit)))
    print(inverted if inverted != 0 else "")


inverter(str(input()))
