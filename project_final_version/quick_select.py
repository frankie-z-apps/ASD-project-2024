import random

# QUICK SELECT (ITERATIVE) WITH RANDOMIZED PIVOT

'''
    Return index of last element in arr
    if arr were to be sorted
'''
def partition(arr, start, end):
    pivot = arr[end-1]
    i = start - 1
    for j in range(start, end-1):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[end-1] = arr[end-1], arr[i+1]
    return i+1


'''
    Return index of arr[i] - where i is randomly chosen - 
    as if arr were ordered    
'''
def rand_partition(arr, start, end):
    i = random.randint(start, end-1)
    arr[end-1], arr[i] = arr[i], arr[end-1]
    return partition(arr, start, end)


'''
    Perform valididy test on parameters and call select algorithm (random pivot)
'''
def quick_select(arr, start, end, k):
    if not(are_parameters_valid(start, end, k)):
        print(f"Index of k({k}) is out of range.\nPlease insert a valid index.")
    else:
        return quick_select_tested(arr, start, end, k)
    

'''
    Perform validity test on parameters and call select algorithm (fixed pivot)
'''
def quick_select_fixed(arr, start, end, k):
    if not(are_parameters_valid(start, end, k)):
        print(f"Index of k({k}) is out of range.\nPlease insert a valid index.")
    else:
        return quick_select_tested_fixed(arr, start, end, k)
    

'''
    Verify that the array is not empty and that the value of k is in array range
'''
def are_parameters_valid(start, end, k):
    return not ((end - start < 1) or (k-1 < start or k-1 > end-1))


'''
    Return the k-th smallest element in arr (without sorting it)
    using the (randomized) partition algorithm.
'''
def quick_select_tested(arr, start, end, k):
    while start < end:
        r = rand_partition(arr, start, end)
        if r == k-1:
            return arr[r]
        elif r > k-1:
            end = r
        else:
            start = r+1
    return arr[start]


'''
    Return the k-th smallest element in arr (without sorting it)
    using the (non-randomized) partition algorithm.
'''
def quick_select_tested_fixed(arr, start, end, k):
    while start < end:
        r = partition(arr, start, end)
        if r == k-1:
            return arr[r]
        elif r > k-1:
            end = r
        else:
            start = r+1
    return arr[start]


if __name__ == "__main__":
        
    def input_array():
        return [int(x) for x in input().split(" ") if x]

    arr = input_array()
    k = int(input())
    print(quick_select(arr, 0, len(arr), k))