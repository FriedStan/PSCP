"""Diamond I"""


def mining(m_depth, n_size):
    """Find the most value daimond's layer"""
    all_depth = [] * bool(n_size)
    for _ in range(m_depth):
        current_layer = str(input()).split()
        current_layer = list(map(int, current_layer))
        all_depth.append(current_layer)
    each_depth_col = list(zip(*all_depth))
    print(sum(sorted(each_depth_col, key=sum, reverse=True)[0]))


mining(int(input()), int(input()))
