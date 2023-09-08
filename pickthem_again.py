"""PickThemAgain"""


def pick_em(num_text):
    """Do as <e>judge says"""
    num_list = num_text.split()
    nope = True
    num_list.reverse()
    for things in num_list:
        things = int(things)
        if things % 3 == 0 or things % 5 == 0:
            print(things)
            nope = False
    if nope is True:
        print("Nope")


pick_em(str(input()))
