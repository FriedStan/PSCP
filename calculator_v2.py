"""Calculator V2"""


def calc_button(num):
    """Count each time the button is placed"""
    if num != 1:
        digit = len(str(num))
        button_pressed = 0
        number_left = num
        for i in range(digit - 1):
            that_much = 9 * (10 ** i)
            button_pressed += ((that_much * (i + 2)))
            number_left -= that_much
        button_pressed += number_left * (digit + 1)
        num = button_pressed
    print(num)

calc_button(int(input()))
