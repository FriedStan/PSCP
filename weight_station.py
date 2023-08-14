"""WeightStation"""


def truck_station(w_list, w_avg):
    """Return the result of the truck test"""
    w_sum = 0
    result = False
    for w_pt in w_list:
        w_sum += w_pt
        if abs(w_avg - w_pt) <= w_avg / 2:
            pass
        else:
            result = "Unbalance"
    if w_sum > 15000:
        result = "Overweight"
    elif result is False:
        result = "Pass {:.2f}".format(w_list[3])
    else:
        pass
    return result


def main():
    """Main func"""
    truck_avg = float(input())
    truck_pt1 = float(input())
    truck_pt2 = float(input())
    truck_pt3 = float(input())
    truck_pt4 = (4 * truck_avg) - (truck_pt1 + truck_pt2 + truck_pt3)
    truck_all = [truck_pt1, truck_pt2, truck_pt3, truck_pt4]
    print(truck_station(truck_all, truck_avg))


main()
