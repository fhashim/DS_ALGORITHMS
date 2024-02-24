def get_direction(lst, midpoint, num):
    # print(lst, midpoint, num)
    # print(lst[midpoint], num)
    if lst[midpoint] == num:
        if len(lst) > 0 and lst[midpoint - 1] == num:
            return 'left'
        else:
            return 'found'
    elif lst[midpoint] == num:
        return 'found'
    elif lst[midpoint] > num:
        return 'left'
    elif lst[midpoint] < num:
        return 'right'
    else:
        return None

def do_binary_search(lst, num):
    # get range of list
    low, high = 0, len(lst) - 1

    if low == high:
        return 0

    # condition to run how long
    while low <= high:
        # get mid value
        midpoint = (low + high) // 2
        direction = get_direction(lst, midpoint, num)

        # you've got the desired position at which number lies
        if direction == 'found':
            return midpoint
        
        # number lies to the left of the list from mid. number is less than the midpoint value
        elif direction == 'left':
            high = midpoint - 1

        # number lies to the right of the list from mid. number is greater than the midpoint value
        elif direction == 'right':
            low = midpoint + 1

        # failed case
        elif direction == None:
            return -1

    return -1

def do_binary_search_reversed(lst, num):
    
    len_list = len(lst) - 1
    lst = lst[::-1]
    position = do_binary_search(lst, num)
    position = len_list - position

    return position


