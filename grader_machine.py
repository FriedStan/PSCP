"""GraderMachine"""


def even_finder(num, pass_text, pass_sum):
    """Find even number"""
    if num % 2 == 0:
        pass_text += " " + str(num)
        pass_sum += num
    else:
        pass
    return pass_text, pass_sum


def selector_machine(start_inp, end_inp):
    """select the even number from start_inp to end_inp """
    pass_text = ""
    pass_sum = 0
    if end_inp >= start_inp:
        for num in range(start_inp, end_inp + 1, 1):
            pass_text, pass_sum = even_finder(num, pass_text, pass_sum)
    else:
        for num in range(start_inp, end_inp - 1, -1):
            pass_text, pass_sum = even_finder(num, pass_text, pass_sum)
    return "pass :{}\n".format(pass_text) +\
           "Sum : {}".format(pass_sum)


print(selector_machine(int(input()), int(input())))
