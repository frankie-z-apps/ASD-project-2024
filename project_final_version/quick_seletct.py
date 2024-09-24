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
    Return index that element at index i (randomly chosen) would occupy
    if arr were to be sorted    
'''
def rand_partition(arr, start, end):
    i = random.randint(start, end-1)
    arr[end-1], arr[i] = arr[i], arr[end-1]
    return partition(arr, start, end)


'''
    Perform valididy test on parameters and call select algorithm
'''
def quick_select(a, start, end, k):
    if not(are_parameters_valid(start, end, k)):
        print(f"Index of k({k}) is out of range.\nPlease insert a valid index.")
    else:
        return quick_select_tested(a, start, end, k)
    

'''
    Verify that the array is not empty and that the value of k is in array range
'''
def are_parameters_valid(start, end, k):
    return not ((end - start < 1) or (k-1 < start or k-1 > end-1))


'''
    Return the k-th smallest element in arr (without sorting it)
    using the (randomized) partition algorithm.
'''
def quick_select_tested(a, start, end, k):
    while start < end:
        r = rand_partition(a, start, end)
        if r == k-1:
            return a[r]
        elif r > k-1:
            end = r
        else:
            start = r+1
    return a[start]


if __name__ == "__main__":
        
    def input_array():
        return [int(x) for x in input().split(" ") if x]

    arr = input_array()
    k = int(input())
    print(quick_select(arr, 0, len(arr), k))