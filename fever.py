'''fever'''


def fever(temp):
    '''indicatehowmuchfever'''
    nofever = (36 <= temp < 38)*"No Fever"
    mild = (38 <= temp < 39)*"Mild Fever"
    high = (39 <= temp < 40)*"High Fever"
    veryhigh = (temp >= 40)*"Very High Fever"
    print(nofever or mild or high or veryhigh)


fever(float(input()))
