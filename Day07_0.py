import sys
sys.path.insert(0, 'input_format')

import Day07_input as input

input_dict = input.format_data()

lowest = next(iter(input_dict))
found = False

while not found:
    found = True
    for node in input_dict:
        _, children = input_dict[node]
        if lowest in children:
            lowest = node
            found = False
            break

print(lowest) 
    