"""Olympic"""


def greatest_medal(country):
    """Display the country that get the most medals then"""
    medal_list = []
    order = 1
    count = 1
    prev = [-1, -1, -1]
    for _ in range(country):
        current = str(input()).split()
        medal_list.append(
            [current[0], [int(current[1]), int(current[2]), int(current[3])]])
    medal_list.sort()
    for things in medal_list:
        things[0], things[1] = things[1], things[0]
    medal_list.sort(reverse=True, key=lambda x: x[0])
    for things in medal_list:
        if prev != things[0]:
            order = count
        print(order, things[1], *things[0], sep=" ", end=" ")
        print(sum(things[0]))
        count += 1
        prev = things[0]


greatest_medal(int(input()))
