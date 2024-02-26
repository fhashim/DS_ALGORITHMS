import random
import time as t
from binary_search import rotate_sorted_list, get_target_position
from brute_force import get_num_position, find_minimum_position_brute_force

def generate_rotated_sorted_list(length):

    # Generate a sorted list of integers
    sorted_list = list(range(length))

    # Choose a random pivot point for rotation
    pivot = random.randint(0, length - 1)

    # Rotate the sorted list to create a rotated sorted list
    rotated_sorted_list = sorted_list[pivot:] + sorted_list[:pivot]

    return rotated_sorted_list

def generate_random_sorted_list(length):

    test_list = [random.randint(0, 1000) for _ in range(length)]
    test_list = sorted(test_list)
    random_number = random.choice(test_list)

    return test_list, random_number

def generate_reversed_random_sorted_list(length):

    test_list, random_number = generate_random_sorted_list(length)
    test_list = test_list[::-1]

    return test_list, random_number

# test_list, random_number = generate_random_sorted_list(1000)
# t0 = t.time()
# position_bs = do_binary_search_reversed(test_list, random_number)
# print(position_bs)
# t1 = t.time()
# print('Binary search algo time: ', (t1-t0)/60)

# t3 = t.time()
# position_brute = get_num_position(test_list, random_number)
# print(position_brute)
# t4 = t.time()
# print('Brute force search algo time: ', (t4-t3)/60)

test_list = [3, 4, 5, 0, 1, 2]
# test_list = generate_rotated_sorted_list(10000)
t5 = t.time()
position_bs = rotate_sorted_list(test_list)
print(position_bs)
t6 = t.time()
print('Binary search algo time: ', (t6-t5)*1000, 'ms')

t7 = t.time()
position_brute = find_minimum_position_brute_force(test_list)
print(position_brute)
t8 = t.time()
print('Brute force search algo time: ', (t8-t7)*1000, 'ms')

test_list = [3, 4, 5, 0, 1, 2]
test_list = [0, 1, 2, 3, 4, 5]
test_list = [5, 0, 1, 2, 3, 4]
test_list = [1]
target = 0
position = get_target_position(test_list, target)
print(position)