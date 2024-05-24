import rand_partition
import random

# QUICK SELECT ITERATIVE VERSION (RANDOMIZED PIVOT)
# note: it seems that without a recursive call
#       the randomization process produces costs,
#       instead of reducing them; and that's
#       because the number of pivots required varies
#       at every call on rand_partition() in the while-loop


def quick_select_iter_rand(a, low, high, k):
    if not(are_parameters_valid(low, high, k)):
        return f"Index of k({k}) is out of range.\nPlease insert a valid index."
    else:
        return iter_quick_select_tested_r(a, low, high, k)
    

# verify that the array is not empty and that the value of k is in array range  
def are_parameters_valid(low, high, k):
    return not ((high - low < 1) or (k-1 < low or k-1 > high-1))


# we're assuming that the parameters are valid
def iter_quick_select_tested_r(a, low, high, k):
    r = rand_partition.rand_partition(a, low, high)
    while r != k-1:
        if r > k-1:
            #print(f"Array: {a}\nValue of r(index): {r}\nValue of a[r]: {a[r]}\nValue of k: {k}\nValue of k-1: {k-1}")
            r = rand_partition.rand_partition(a, low, r)
            #print(f"Array: {a}\nValue of r(index): {r}\nValue of a[r]: {a[r]}\nValue of k: {k}\nValue of k-1: {k-1}")
        else:
            #print(f"Array: {a}\nValue of r(index): {r}\nValue of a[r]: {a[r]}\nValue of k: {k}\nValue of k-1: {k-1}")
            r = rand_partition.rand_partition(a, r+1, high)
            #print(f"Array: {a}\nValue of r(index): {r}\nValue of a[r]: {a[r]}\nValue of k: {k}\nValue of k-1: {k-1}")
    return a[r]


def input_array():
    return [int(x) for x in input().split(" ") if x]


'''
a = input_array()
k = int(input())
print(quick_select_iter_rand(a, 0, len(a), k))
#'''


'''
arr = [0] * 1000000

for i in range(len(arr)):
    arr[i] = random.randint(-1000000, 1000000)

for i in range(1):
    a =  arr.copy()
    print(a)
    print(quick_select_iter_rand(a, 0, len(a), 10))
#'''