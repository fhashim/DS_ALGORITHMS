def get_num_position(lst, num):

    for i in range(0, len(lst)):
        if lst[i] == num:
            return i
    return -1

def find_minimum_position_brute_force(lst):
    # Handling special cases
    if not lst:
        return -1
    if len(lst) == 1:
        return 0

    # Iterate through the list to find the minimum element and its position
    minimum = lst[0]
    min_position = 0
    for i in range(len(lst)):
        if lst[i] < minimum:
            minimum = lst[i]
            min_position = i
    return min_position
