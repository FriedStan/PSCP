"""GCD_N"""


def personal_gcd(num1, num2):
    """My very own gcd"""
    while num2 != 0:
        temp = num1 % num2
        num1 = num2
        num2 = temp
    return num1


def gcd_n(n_unit):
    """Find the gcd of n numbers"""
    num_list = []
    for _ in range(n_unit):
        num_list.append(int(input()))
    if n_unit != 1:
        num1 = num_list[0]
        num2 = num_list[1]
        current_gcd = personal_gcd(num1, num2)
        for i in range(2, len(num_list)):
            current_gcd = personal_gcd(current_gcd, num_list[i])
        print(current_gcd)
    else:
        print(*num_list)


gcd_n(int(input()))
