"""ProgressiveTax"""


def taxtifyer(income):
    """Tax your income"""
    if 0 <= income <= 150000:
        tax = 0
    elif 150000 < income <= 300000:
        diff = income - 150000
        income -= diff
        tax = (5 / 100) * diff
    elif 300000 < income <= 500000:
        diff = income - 300000
        income -= diff
        tax = (10 / 100) * diff
    elif 500000 < income <= 750000:
        diff = income - 500000
        income -= diff
        tax = (15 / 100) * diff
    elif 750000 < income <= 1000000:
        diff = income - 750000
        income -= diff
        tax = (20 / 100) * diff
    elif 1000000 < income <= 2000000:
        diff = income - 1000000
        income -= diff
        tax = (25 / 100) * diff
    elif 2000000 < income <= 4000000:
        diff = income - 2000000
        income -= diff
        tax = (30 / 100) * diff
    elif income > 4000000:
        diff = income - 4000000
        income -= diff
        tax = (35 / 100) * diff
    else:
        tax = 0
    return tax, income


def taxer(income):
    """Calculate user tax"""
    tax = 0
    while income > 150000:
        get_tax, income = taxtifyer(income)
        tax += get_tax
    return int(tax)


print(taxer(float(input())))
