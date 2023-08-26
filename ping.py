"""Pong"""


def where_did_you_ping(pinging, space, ping_status_01):
    """Get What user is pinging"""
    domain = space
    domain = pinging[pinging.find("ping ") + 5:]
    domain_nodot = domain.replace(".", "")
    if not domain_nodot.isdigit():
        left_bracket = ping_status_01.find("[")
        right_bracket = ping_status_01.find("]")
        domain = ping_status_01[left_bracket + 1:right_bracket]
    line_01 = "Ping statistics for {}:".format(domain)
    return line_01


def packet_checker(packet_01, packet_02, packet_03, packet_04):
    """Check if all the packets is """
    time_01_ms = packet_01.find("ms")
    time_02_ms = packet_02.find("ms")
    time_03_ms = packet_03.find("ms")
    time_04_ms = packet_04.find("ms")
    time_01 = packet_01[packet_01.find(" time") + 5:time_01_ms]
    time_02 = packet_02[packet_02.find(" time") + 5:time_02_ms]
    time_03 = packet_03[packet_03.find(" time") + 5:time_03_ms]
    time_04 = packet_04[packet_04.find(" time") + 5:time_04_ms]
    if time_01_ms == -1:
        time_01 = "-1"
    if time_02_ms == -1:
        time_02 = "-1"
    if time_03_ms == -1:
        time_03 = "-1"
    if time_04_ms == -1:
        time_04 = "-1"
    return get_actual_time(time_01, time_02, time_03, time_04)


def get_actual_time(time_01, time_02, time_03, time_04):
    """Transform the time from package into actual readable time"""
    if time_01[0] == "=":
        time_01 = int(time_01[1:])
    elif time_01[0] == "<":
        time_01 = 0
    if time_02[0] == "=":
        time_02 = int(time_02[1:])
    elif time_02[0] == "<":
        time_02 = 0
    if time_03[0] == "=":
        time_03 = int(time_03[1:])
    elif time_03[0] == "<":
        time_03 = 0
    if time_04[0] == "=":
        time_04 = int(time_04[1:])
    elif time_04[0] == "<":
        time_04 = 0
    return int(time_01), int(time_02), int(time_03), int(time_04)


def find_loss(time_01, time_02, time_03, time_04):
    """Find the percentage of loss"""
    loss = 0
    if time_01 < 0:
        loss += 1
    if time_02 < 0:
        loss += 1
    if time_03 < 0:
        loss += 1
    if time_04 < 0:
        loss += 1
    loss_percent = int(loss * 100 / 4)
    line_02 = "    Packets: Sent = 4, Received = {}, Lost = {} ({}% loss),"\
        .format(4 - loss, loss, int(loss_percent))
    return line_02


def find_minmaxavg(time_01, time_02, time_03, time_04):
    """Find the average of time"""
    average = -1
    if time_01 != -1 or time_02 != -1 or time_03 != -1 or time_04 != -1:
        time_01_sent = time_01 != -1
        time_02_sent = time_02 != -1
        time_03_sent = time_03 != -1
        time_04_sent = time_04 != -1
        average_top = (time_01 * time_01_sent) + (time_02 * time_02_sent) + \
            (time_03 * time_03_sent) + (time_04 * time_04_sent)
        average_bot = (1 * time_01_sent) + (1 * time_02_sent) + \
                      (1 * time_03_sent) + (1 * time_04_sent)
        average = int(average_top / average_bot)
        min_time = min(time_01 + ((not time_01_sent) * 999), time_02 + ((not time_02_sent) * 999),
                       time_03 + ((not time_03_sent) * 999), time_04 + ((not time_04_sent) * 999))
        max_time = max(time_01, time_02, time_03, time_04)
        print("Approximate round trip times in milli-seconds:\n" +
              "    Minimum = {}ms, Maximum = {}ms, Average = {}ms"\
                .format(min_time, max_time, average))
    else:
        pass


def return_to_sender():
    """Output the log of pinging"""
    line_01 = where_did_you_ping(str(input()), str(input()), str(input()))
    time_01, time_02, time_03, time_04 = packet_checker(
        str(input()), str(input()), str(input()), str(input()))
    line_02 = find_loss(time_01, time_02, time_03, time_04)
    print(line_01 + "\n" + line_02)
    find_minmaxavg(time_01, time_02, time_03, time_04)


return_to_sender()
