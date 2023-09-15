"""Divide3Or5"""


def devide_3or5(num):
    """หาผลรวมของจำนวนเต็มตั้งแต่ 1 จนถึงตัวเลขที่กำหนดที่หารด้วย 3 หรือ 5 ลงตัว"""
    num_list = filter(lambda x: 0 in (x % 3, x % 5), list(range(1, int(num) + 1)))
    print(sum(num_list))


devide_3or5(float(input()))
