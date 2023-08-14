"""Food Grade 1"""


def chicken(count, valid_wing):
    """Compare data"""
    if count < 24:
        w_inp = int(input())
        if 50 <= w_inp <= 70:
            count += 1
            valid_wing += 1
            chicken(count, valid_wing)
        else:
            count += 1
            chicken(count, valid_wing)
    else:
        print(valid_wing)


def main():
    """Main Func"""
    chicken(0, 0)


main()
