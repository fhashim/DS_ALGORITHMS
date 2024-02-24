def get_num_position(lst, num):

    for i in range(0, len(lst)):
        if lst[i] == num:
            return i
    return -1