"""GCD_v1"""


def find_gcd(num_1, num_2):
    """Find the GCD of 2 numbers"""
    maxine = max(num_1, num_2)
    for num in range(1, min(num_1, num_2) + 1):
        if num_1 % num == num_2 % num == 0:
            maxine = num
    print(maxine)


find_gcd(int(input()), int(input()))
