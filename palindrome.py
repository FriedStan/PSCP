"""[Midterm 2022] Palindrome"""


def palindromer(n_times, time):
    """Tell the next n times palin"""
    current_time = time.replace(":", "")
    while len(current_time) < 4:
        current_time = "0" + current_time
    hour = int(current_time[:2])
    less_than_hour_more_than_sec = int(current_time[2:])
    while n_times > 0:
        less_than_hour_more_than_sec += 1
        if less_than_hour_more_than_sec >= 60:
            less_than_hour_more_than_sec -= 60
            hour += 1
        if hour >= 24:
            hour -= 24
        current_time = "{:2d}{:02d}".format(hour, less_than_hour_more_than_sec).strip()
        if current_time == current_time[::-1]:
            if len(str(hour)) < 2:
                print(current_time[:1] + ":" + current_time[1:])
            else:
                print(current_time[:2] + ":" + current_time[2:])
            n_times -= 1


palindromer(int(input()), str(input()))
