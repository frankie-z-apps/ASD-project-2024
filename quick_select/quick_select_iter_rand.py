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
    while low < high:
        r = rand_partition.rand_partition(a, low, high)
        if r == k-1:
            return a[r]
        elif r > k-1:
            high = r
        else:
            low = r+1
    return a[low]



if __name__ == "__main__":
        
    def input_array():
        return [int(x) for x in input().split(" ") if x]

    a = input_array()
    k = int(input())
    print(quick_select_iter_rand(a, 0, len(a), k))