"""Hamming"""
print(sum(a != b for a, b in zip(str(input()), str(input()))))
