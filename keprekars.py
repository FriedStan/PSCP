"""Kaprekars"""


def my_mc(num_1, num_2):
    """My own max"""
    return num_1 if num_1 >= num_2 else num_2


def my_low(num_1, num_2):
    """My own max"""
    return num_1 if num_1 <= num_2 else num_2


def keprekars(keprekars_num):
    """Count how many times you have to use Kaprekars method"""
    salted = ""
    for _ in range(len(keprekars_num)):
        for num_1 in keprekars_num:
            next_num = num_1
            current = int(num_1) - 1
            current = my_mc(int(current), int(next_num))   
        keprekars_num = keprekars_num.replace(str(current), "")
        salted += str(current)
    print(salted)


keprekars(str(input()))
