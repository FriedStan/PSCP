"""Socks"""


def sock_suck(unpaired_sock):
    """Socks"""
    paired_sock = []
    sock_count = {}
    for sock in unpaired_sock:
        sock_count[sock] = sock_count.get(sock, 0) + 1
    for sock, amount in sock_count.items():
        paired_sock.extend([sock*2 for _ in range(amount // 2)])
    if paired_sock:
        print(*sorted(paired_sock))
    else:
        print("None")
    print(len(paired_sock))


sock_suck(list(str(input())))
