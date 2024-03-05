from collections import OrderedDict, deque

ordered_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

order_queue = deque(ordered_dict)
new_key = 'z'
new_value = 100
order_queue.appendleft(new_key)
ordered_dict.move_to_end(new_key, last=False) 
ordered_dict[new_key] = new_value

print(ordered_dict)