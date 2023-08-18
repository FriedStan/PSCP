"""Phone number"""


def phone(phone_num, phone_type):
    """Format the phone number to correct format"""
    phone_size = len(phone_num)
    if phone_size == 9:
        phone_num = phone_num[:1] + " " + phone_num[1:5] + " " + phone_num[5:9]
    elif phone_size == 10:
        phone_num = phone_num[:2] + " " + phone_num[2:6] + " " + phone_num[6:10]
    if phone_type.title() == "Domestic":
        print(phone_num)
    elif phone_type.title() == "International":
        print(phone_num.replace("0", "+66", 1))


phone(str(input()), str(input()))
