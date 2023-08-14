"""https://open.spotify.com/track/3kC1ggozqeY847x7fOFqAl?si=1d15d73ea6fe4e76"""


def main():
    """Main func"""
    sec_inp = float(input())
    sec = sec_inp
    minute = sec // 60
    sec %= 60
    hrs = minute // 60
    minute %= 60
    day = hrs // 24
    hrs %= 24
    print("%04d:%02d:%02d:%02d" % (day, hrs, minute, sec) if day < 10000 else "ERR_:__:__:__")


main()
