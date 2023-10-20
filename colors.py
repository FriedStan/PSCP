"""Colors"""


def coloring(color_a, color_b):
    """Combine colors"""
    cheat_sheet = {
        "Red": {
            "Yellow": "Orange",
            "Blue": "Violet",
            "Red": "Red"
        },
        "Blue": {
            "Yellow": "Green",
            "Red": "Violet",
            "Blue": "Blue"
        },
        "Yellow": {
            "Red": "Orange",
            "Blue": "Green",
            "Yellow": "Yellow"
        }
    }
    print(cheat_sheet.get(color_a, {"No": 0}).get(color_b, "Error"))


coloring(str(input()).title(), str(input()).title())
