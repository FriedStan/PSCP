"""[Midterm 2021] MAC"""


def strip_mac(mac_address):
    """Remove every things that is not alphanumerical"""
    out = ""
    for things in mac_address:
        if things.isalnum():
            out += things
    return out


def which_method(mac_address, this_char):
    """Find out what's method this mac address is using"""
    mac_strip = strip_mac(mac_address)
    current_method = ""
    if this_char in "-:":
        current_method = "{1}{0}{2}{0}{3}{0}{4}{0}{5}{0}{6}".format(
            this_char, mac_strip[:2], mac_strip[2:4], mac_strip[4:6]\
                , mac_strip[6:8], mac_strip[8:10], mac_strip[10:12])
    else:
        current_method = "{1}{0}{2}{0}{3}".format(
            this_char, mac_strip[:4], mac_strip[4:8], mac_strip[8:12])
    return mac_address == current_method


def mac_or_not(mac_address):
    """Return that the input is a valid mac address or not"""
    mac_strip = strip_mac(mac_address)
    error = False
    for things in mac_strip:
        if things not in "0123456789ABCDEF" or len(mac_strip) != 12:
            error = True
    if error is False:
        method_1 = which_method(mac_address, "-")
        method_2 = which_method(mac_address, ":")
        method_3 = which_method(mac_address, ".")
        valid = method_1 or method_2 or method_3
        out = "VALID " * valid + "1" * method_1 + "2" * method_2 + "3" * method_3
    else:
        out = "ERROR"
    print(out if out != "" else "ERROR")


mac_or_not(str(input()).upper())
