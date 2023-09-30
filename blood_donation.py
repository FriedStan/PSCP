"""BloodDonation"""


def can_u_donate(age, weight, been_here):
    """Tell that you can donate your blood"""
    valid_age = 17 <= age <= 70
    valid_weight = weight >= 45
    first_time = (been_here == 0 and age <= 55) or bool(been_here)
    permission = True #default permission
    if age == 17 or 60 <= age <= 70:
        permission = str(input()) == "True"
    print("Yes" if valid_age and valid_weight and first_time and permission else "No")


can_u_donate(int(input()), int(input()), int(input()))
