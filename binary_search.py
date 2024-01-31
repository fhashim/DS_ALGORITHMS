def get_location(list, number, mid):
    print('List:', list, 'Number:', number, 'Mid:', mid)
    if number == list[mid]:
        if mid-1 >= 0 and number == list[mid-1]:
            return 'left'
        else:
            return 'found'
    elif number > list[mid]:
        return 'left'
    else:
        return 'right'

def find_number(list, number):
    low, high = 0, len(list) - 1

    while low <= high:
        print('low:', low, 'high:', high)
        mid = (low + high) // 2
        result = get_location(list, number, mid)
        print('Result', result)

        if result == 'found':
            return mid
        elif result == 'right':
            low = mid + 1
        elif result == 'left':
            high = mid - 1 

    return -1

find_number([10, 5, 5, 3, 1], 5)