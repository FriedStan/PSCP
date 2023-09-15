"""isprime_small"""


def is_it_prime(num):
    """Do as function says"""
    prime = "Yes"
    if num % 2 != 0 and num != 1:
        for i in range(2, num // 2):
            if num % i == 0:
                prime = "No"
                break
    elif (num % 2 == 0 and num != 2) or num == 1:
        prime = "No"
    print(prime)


is_it_prime(int(input()))
