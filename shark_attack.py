"""เห็นทะเลยังเป็นหน้าเธอ มันละเมอคิดถึงเธอทุกที"""


def larking(text):
    """Do as <e>judge says"""
    data = {"BULL SHARK": 0,
            "CHAIN CATSHARK": 1,
            "GREAT WHITE SHARK": 1,
            "GUMMY SHARK": 1,
            "BLUE SHARK": 1,
            "MAKO SHARK": 1,
            "FRILLED SHARK": 2,
            "GOBLIN SHARK": 2,
            "SIXGILL SHARK": 2,
            "GREENLAND SHARK": 2,
            "COOKIECUTTER SHARK": 2,
            "MEGAMOUTH SHARK": 3}
    depth = ("THE SHALLOW ZONE", "THE TWILIGHT ZONE", "THE MIDNIGHT ZONE",
             "THE ABYSSAL ZONE", "ZONE JAI MA KLUNG RAK DUAY KAN MAI.")
    print(depth[data.get(text, 4)] if "SHARK" in text else depth[4])


larking(str(input()).upper())
