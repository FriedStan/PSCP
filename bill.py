"""Bill Cypher"""


def biller(payment):
    """Calculate amount that customer needs to pay"""
    service_charge = (payment * 10) / 100
    if service_charge < 50:
        service_charge = 50
    elif service_charge > 1000:
        service_charge = 1000
    vat = ((payment + service_charge) * 7) / 100
    return "{:.2f}".format(payment + service_charge + vat)


print(biller(int(input())))
