"""SMS"""


def sms_maker(count):
    """Make a sms text by sms keyboard"""
    out_put = []
    button_dict = {2:"ABC", 3:"DEF", 4:"GHI", 5:"JKL",
                   6:"MNO", 7:"PQRS", 8:"TUV", 9:"WXYZ"}
    for _ in range(count):
        button = int(input())
        press = int(input())
        if button == 1:
            del out_put[max(len(out_put) - press, 0):]
        else:
            that_seq = button_dict.get(button)
            out_put.append(that_seq[(press % len(that_seq)) - 1])
    if out_put:
        print(*out_put, sep="")
    else:
        print("null")


sms_maker(int(input()))
