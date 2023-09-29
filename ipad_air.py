"""iPad Air"""


def ipad(color, size, connect):
    """Ipad calc"""
    catalog = {"color": ["Space Gray", "Silver", "Green", "Rose Gold", "Sky Blue"],
               64: {"Wi-Fi": 19900, "Wi-Fi + Cellular": 24400},
               256: {"Wi-Fi": 24900, "Wi-Fi + Cellular": 29400}}
    valid_size = catalog.get(size)
    if valid_size is not None and (color in catalog.get("color")):
        print(valid_size.get(connect) or "Not Available")
    else:
        print("Not Available")


ipad(str(input()), int(input()), str(input()))
