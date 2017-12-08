import sys
sys.path.insert(0, 'input_format')

import Day07_input as input

def find_lowest(dict_tree):
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
    return lowest

def sum_weigths(dict_tree, node):
    weight, children = dict_tree[node]
    weight_sum = weight
    for child in children:
        weight_sum += sum_weigths(dict_tree, child)
    dict_tree[node] = (weight_sum, children)
    return weight_sum    

input_dict = input.format_data()

root = find_lowest(input_dict)

sum_weigths(input_dict, root)

leaves_dict = {}

for node in input_dict:
    weight, children = input_dict[node]
    if not children:
        if weight in leaves_dict:
            leaves_dict[weight].append(node)
        else:
            leaves_dict[weight] = [node]

print(leaves_dict)
    