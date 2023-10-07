import random
some = True
while some:
    C = str(random.randrange(0, 8))
    B = str(random.randrange((int(C) + 1), 9))
    A = str(random.randrange((int(B) + 1), 10))
    some = int(A+B+C) - int(C+B+A) == int(C+A+B)
print(some, A, B, C)