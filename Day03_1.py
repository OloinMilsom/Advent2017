from itertools import count

def get_new_val(a, i, j):
    return sum(a.get((k,l), 0) for k in range(i-1,i+2) for l in range(j-1,j+2))

def sum_spiral():
    a, i, j = {(0,0) : 1}, 0, 0

    for s in count(1, 2):
        # right
        for _ in range(s):   
            i += 1 
            a[i,j] = get_new_val(a,i,j)
            yield a[i,j]
        # up
        for _ in range(s):   
            j -= 1
            a[i,j] = get_new_val(a,i,j)
            yield a[i,j]
        # left
        for _ in range(s+1):
            i -= 1
            a[i,j] = get_new_val(a,i,j)
            yield a[i,j]
        # down
        for _ in range(s+1): 
            j += 1
            a[i,j] = get_new_val(a,i,j)
            yield a[i,j]

def main(n):
    for x in sum_spiral():
        if x > n: 
            return x

print(main(361527))