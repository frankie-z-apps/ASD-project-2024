import quick_select.rand_partition as rand_partition

# QUICK SELECT RECURSIVE VERSION (RANDOMIZED PIVOT)


def quick_select_rec_rand(a, low, high, k):
    if not(are_parameters_valid(low, high, k)):
        return f"Index of k({k}) is out of range.\nPlease insert a valid index."
    else:
        return quick_select_tested(a, low, high, k)
    

# verify that the array is not empty and that the value of k is in array range  
def are_parameters_valid(low, high, k):
    return not ((high - low < 1) or (k-1 < low or k-1 > high-1))


def quick_select_tested(a, low, high, k):                     
    r = rand_partition.rand_partition(a, low, high)
    # base case -> chosen pivot is the searched value, return element in this position
    if r == k-1: 
        return a[r]
    # recursive call left/right-wise depending on the value of chosen pivot
    elif r > k-1: 
        return quick_select_tested(a, low, r, k)
    else: 
        return quick_select_tested(a, r+1, high, k)

'''
def partition(a, low, high):
    p = a[high-1]
    i = low
    for j in range(low, high-1):
        if a[j] <= p:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[high-1] = a[high-1], a[i]
    return i 
'''
'''
def rand_partition(a, low, high):
    i = random.randint(low, high-1)
    a[high-1], a[i] = a[i], a[high-1]
    return partition(a, low, high)
'''

#'''Tests:
'''
arr = [5, 4, 3, 2, 1]
print(quick_select_rec(arr, 0, len(arr), 2))
print(quick_select_rec(arr, 0, len(arr), 4))
print(quick_select_rec(arr, 0, len(arr), 6))
'''
#'''


def input_array():
    return [int(x) for x in input().split(" ") if x]

'''
a = input_array()
k = int(input())
print(quick_select_rec_rand(a, 0, len(a), k))
'''