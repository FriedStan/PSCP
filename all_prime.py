"""All_Primes"""


def is_it_prime(num):
    """Do as function says"""
    prime = True
    if num % 2 != 0 and num != 1:
        for i in range(2, num // 2):
            if num % i == 0:
                prime = False
                break
    elif (num % 2 == 0 and num != 2) or num == 1:
        prime = False
    return prime


def prime_count(num):
    """count the prime until num number"""
    count = 0
    for i in range(2, num + 1):
        if is_it_prime(i):
            count += 1
    print(count)


prime_count(int(input()))
