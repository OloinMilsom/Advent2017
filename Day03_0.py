import math

input = 361527

def find_ring(x):
    return (math.floor(math.sqrt(x)) + 1) // 2

def find_distance_for_ring(ring_num, num):
    max = ring_num
    min = 0
    
    ascending = False

    index = num - ((2*ring_num-1) * (2*ring_num-1))
    current = ring_num - 1

    for n in range(0, index):
        if current == max or current == min:
            ascending = not ascending
        if ascending:
            current = current + 1            
        else:
            current = current - 1

    return current        

ring_num = find_ring(input-1)
distance_for_ring = find_distance_for_ring(ring_num, input-1)

print(ring_num + distance_for_ring)