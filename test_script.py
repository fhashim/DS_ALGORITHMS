import random
import time as t
from binary_search import do_binary_search_reversed
from brute_force import get_num_position

test_list = [random.randint(0, 1000) for _ in range(10000000)]
test_list = sorted(test_list)[::-1]
random_number = random.choice(test_list)

t0 = t.time()
position_bs = do_binary_search_reversed(test_list, random_number)
print(position_bs)
t1 = t.time()
print('Binary search algo time: ', (t1-t0)/60)

t3 = t.time()
position_brute = get_num_position(test_list, random_number)
print(position_brute)
t4 = t.time()
print('Brute force search algo time: ', (t4-t3)/60)

position = do_binary_search_reversed([3,2,1,0], 3)
print(position)
