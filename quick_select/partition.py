# return the index of the last element of the array
# if the same array was to be sorted
def partition(arr, low, high):
    pivot = arr[high-1]
    #print(f"pivot : {pivot}, arr[{high-1}]")
    i = low - 1

    iterations=0

    for j in range(low, high-1):
        iterations += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    #print(f"Total iterations: {iterations}")
    arr[i+1], arr[high-1] = arr[high-1], arr[i+1]
    return i+1

'''
arr = [0, 9, 1, 8, 2, 7, 3, 6, 4, 5]
print(partition(arr, 0, len(arr)))
'''
