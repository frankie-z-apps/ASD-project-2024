def partition(arr, low, high):
    pivot = arr[high-1]  
    i = low - 1        

    for j in range(low, high-1):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high-1] = arr[high-1], arr[i+1]
    return i+1