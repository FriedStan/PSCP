"""Kaprekars"""


def my_mc(num_1, num_2):
    """My own max"""
    return num_1 if num_1 >= num_2 else num_2


def my_low(num_1, num_2):
    """My own min"""
    return num_1 if num_1 <= num_2 else num_2


def my_sod_mc(keprekars_num):
    """Sorted the number descendant"""
    salted = ""
    for _ in range(len(keprekars_num)):
        biggest = -1
        for num in keprekars_num:
            biggest = my_mc(biggest, int(num))
        keprekars_num = keprekars_num.replace(str(biggest), "", 1)
        salted += str(biggest)
    return int(salted)


def my_sod_low(keprekars_num):
    """Sorted the number ascendant"""
    unsalted = ""
    for _ in range(len(keprekars_num)):
        smallest = 10
        for num in keprekars_num:
            smallest = my_low(smallest, int(num))
        keprekars_num = keprekars_num.replace(str(smallest), "", 1)
        unsalted += str(smallest)
    return int(unsalted)


def keprekars(keprekars_num):
    """Count how many times you have to use Kaprekars method"""
    the_6174 = 0
    count = 0
    while the_6174 != 6174:
        while len(keprekars_num) < 4:
            keprekars_num += "0"
        salted = my_sod_mc(keprekars_num)
        unsalted = my_sod_low(keprekars_num)
        the_6174 = salted - unsalted
        keprekars_num = str(the_6174)
        count += 1
    print(count)


keprekars(str(input()))
