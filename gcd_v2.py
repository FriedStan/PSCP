"""GCD_v2"""


def let_gcd(num_1, num_2):
    """Find the GCD"""
    while num_2 != 0:
        temp = num_1 % num_2
        num_1 = num_2
        num_2 = temp
    print(num_1)


let_gcd(int(input()), int(input()))
