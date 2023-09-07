"""[Midterm 2023] Ticket Fare"""


def my_mac(num1, num2):
    """My own max"""
    return num1 if num1 >= num2 else num2


def my_meen(num1, num2):
    """My own min"""
    return num1 if num1 <= num2 else num2


def tier_1_fare(a_pt, b_pt, trip_left, fare):
    """Add tier 1 fare"""
    trip_left -= a_pt
    trip_left = my_mac(trip_left, 0)
    fare = b_pt
    return trip_left, fare


def tier_2_fare(c_pt, d_pt, trip_left, fare):
    """Add tier 2 fare"""
    tier2_trip = my_meen(c_pt, trip_left)
    fare += tier2_trip * d_pt
    trip_left -= tier2_trip
    trip_left = my_mac(trip_left, 0)
    return trip_left, fare


def fare_calc():
    """Calculate ticket fare"""
    n_pt = int(input())
    a_pt = int(input())
    b_pt = int(input())
    c_pt = int(input())
    d_pt = int(input())
    e_pt = int(input())
    f_pt = int(input())
    g_pt = int(input())
    trip_left = abs(f_pt - g_pt)
    if f_pt == g_pt:
        trip_left = 1
    fare = 0
    if f_pt <= n_pt and g_pt <= n_pt:
        trip_left, fare = tier_1_fare(a_pt, b_pt, trip_left, fare)
        trip_left, fare = tier_2_fare(c_pt, d_pt, trip_left, fare)
        fare += trip_left * e_pt
        print(fare)
    else:
        print("Error")


fare_calc()
