"""[Midterm 2021] Solar System"""


def make_a_seq(text):
    """Change the text to a sequence"""
    text = " " + text + " "
    return text.replace(" ", "|")


def find_the_sun(text_seq):
    """Find the sun position"""
    sun_pos = text_seq.find("|Sun|")
    return sun_pos


def right_left_sun(sun_pos, text_seq, text_seq_rev):
    """If the Sun is in the right"""
    hottest, coolest = "", ""
    count = 0
    for things in text_seq_rev:
        if things == "|":
            count += 1
            if count >= 3:
                break
        elif count == 2:
            if sun_pos == "right":
                hottest += things
            else:
                coolest += things
    count = 0
    for things in text_seq:
        if things == "|":
            count += 1
            if count >= 2:
                break
        elif count <= 1:
            if sun_pos == "right":
                coolest += things
            else:
                hottest += things
    return hottest[::-1], coolest


def notlr_sun(sun_pos, text_seq):
    """If the sun is not left or right"""
    text_left = text_seq[1:sun_pos]
    text_right = text_seq[sun_pos + 5:len(text_seq) - 1]
    planet_left = text_left.count("|")
    planet_right = text_right.count("|")
    coolest, hottest = "", ""
    if planet_left > planet_right:
        coolest = text_left[:text_left.find("|")]
    elif planet_right > planet_left:
        coolest = text_right[::-1][:text_right[::-1].find("|")][::-1]
    else:
        coolest = text_left[:(text_left + "|").find("|")] + " "\
            + text_right[::-1][:(text_right[::-1] + "|").find("|")][::-1]
    hottest = text_left[::-1][:(text_left[::-1] + "|").find("|")][::-1] + " "\
        + text_right[:(text_right + "|").find("|")]
    #print(text_left, text_right)
    return hottest, coolest


def cooler_or_hotter(text):
    """Find the coolest and the hottest planet"""
    text_seq = make_a_seq(text)
    text_seq_rev = text_seq[::-1]
    sun_pos = find_the_sun(text_seq)
    hottest = ""
    coolest = ""
    if sun_pos + 5 == len(text_seq):
        # sun pos = right
        hottest, coolest = right_left_sun("right", text_seq, text_seq_rev)
    elif sun_pos == 0:
        # sun pos = left
        coolest, hottest = right_left_sun("left", text_seq_rev, text_seq)
    else:
        # sun pos = not left, right
        hottest, coolest = notlr_sun(sun_pos, text_seq)
    print("Hot: {}".format(hottest))
    print("Cool: {}".format(coolest))


cooler_or_hotter(str(input()))
