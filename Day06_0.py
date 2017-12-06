input = [11, 11, 13, 7, 0, 15, 5, 5, 4, 4, 1, 1, 7, 1, 15, 11]

def balance_list(int_list):
    maximum = max(int_list)
    max_index = int_list.index(maximum)
    int_list[max_index] = 0
    for i in range(maximum):
        curr_index = max_index + i + 1
        while curr_index >= len(int_list):
            curr_index -= len(int_list)
        int_list[curr_index] += 1
    return int_list

curr = input
visited = []
steps = 0

while str(curr) not in visited:
    visited.append(str(curr))
    curr = balance_list(curr)
    steps += 1

print(steps)