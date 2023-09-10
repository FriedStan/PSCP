"""AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain"""


def again_again(text):
    """Do as <e>judge says"""
    text_list = text.replace(".", "").split()
    text_list.sort()
    vowel = "aeiou"
    have_print = False
    for things in text_list:
        count = 0
        for char in things:
            if char.lower() in vowel:
                count += 1
        if count >= 2:
            print(things)
            have_print = True
    if have_print is False:
        print("Nope")


again_again(str(input()))
