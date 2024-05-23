import random

# QUICK SELECT ITERATIVE VERSION (FIXED PIVOT)


def quick_select_iter_fixed(a, low, high, k):
    if not(are_parameters_valid(low, high, k)):
        return f"Index of k({k}) is out of range.\nPlease insert a valid index."
    else:
        return iter_quick_select_tested(a, low, high, k)
    

# verify that the array is not empty and that the value of k is in array range  
def are_parameters_valid(low, high, k):
    return not ((high - low < 1) or (k-1 < low or k-1 > high-1))


# we're assuming that the parameters are valid
def iter_quick_select_tested(a, low, high, k):
    r = partition(a, low, high)
    while r != k-1:
        if r > k-1:
            r = partition(a, low, r)
        else:
            r = partition(a, r+1, high)
    return a[r]


def partition(a, low, high):
    p = a[high-1]
    i = low
    for j in range(low, high-1):
        if a[j] <= p:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[high-1] = a[high-1], a[i]
    return i 


def rand_partition(a, low, high):
    i = random.randint(low, high-1)
    a[high-1], a[i] = a[i], a[high-1]
    return partition(a, low, high)


def input_array():
    return [int(x) for x in input().split(" ") if x]

'''
a = input_array()
k = int(input())
print(quick_select_iter_fixed(a, 0, len(a), k))
'''