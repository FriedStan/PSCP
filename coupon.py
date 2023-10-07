"""Coupon"""


def coupon_comparer(org_price, coupon_1, coupon_2):
    """Compare the discount!"""
    discount_1 = org_price - \
        coupon_1[0] if org_price >= coupon_1[1] else org_price
    discount_2 = org_price * \
        (1 - (coupon_2[0] / 100)) if org_price >= coupon_2[1] else org_price
    get_no_discount = (discount_1 == org_price) and (discount_2 == org_price)
    coupon = {1: "1 {:.1f}".format(discount_1),
              2: "2 {:.1f}".format(discount_2)}
    text = (coupon.get(1) * (discount_1 < discount_2)) or\
           (coupon.get(2) * (discount_1 > discount_2)) or (get_no_discount * "Nope")
    if text == "":
        text = (coupon.get(1) * (coupon_1[1] <= coupon_2[1])) or\
            (coupon.get(2) * (coupon_1[1] > coupon_2[1]))
    print(text)


coupon_comparer(float(input()),
                tuple(map(float, str(input()).split())),
                tuple(map(float, str(input()).split())))
