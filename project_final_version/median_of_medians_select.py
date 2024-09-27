# MEDIAN OF MEDIANS SELECT


# sort in ascending order
# the sub-array arr[start, end]
def insertion_sort(arr, start, end):
    for i in range(start+1, end):
        key = arr[i]
        j = i-1
        while j >= start and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


# return index of arr[r] as if arr were ordered
def partition_med(arr, start, end, r):
    pivot = arr[r]
    arr[r], arr[end-1] = arr[end-1], arr[r]
    i = start - 1

    for j in range(start, end-1):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[end-1] = arr[end-1], arr[i+1]
    return i + 1


# return index of median element in sub-array arr[start, end]
def median(arr, start, end):
    insertion_sort(arr, start, end)
    relative_next_median_index = (end - start) // 2
    absolute_next_median_index = start + relative_next_median_index
    return absolute_next_median_index


'''
    Return the k-th smallest element in arr (without sorting it) 
    making use of the median of medians algorithm.
'''
def median_of_medians_select(arr, start, end, k):
    while start <= end:
        m = median_of_medians(arr, start, end)
        r = partition_med(arr, start, end, m)

        if r > k-1:
            end = r
        elif r < k-1:
            start = r+1
        else:
            return arr[r]
        
    print("Index Error!")


# return index of median element in sub-array arr[start,end]
def median_of_medians(arr, start, end):
    if end - start > 5:
        next_median_index = start

        for i in range(start, end, 5):
            if i + 5 <= end:
                current_median = median(arr, i, i+5)
            else:
                current_median = median(arr, i, end)
            
            arr[next_median_index], arr[current_median] = arr[current_median], arr[next_median_index]
            next_median_index += 1
        
        return median_of_medians(arr, start, next_median_index)
    else:
        return median(arr, start, end)


if __name__ == "__main__":
        
    def input_array():
        return [int(x) for x in input().split(" ") if x]

    a = input_array()
    k = int(input())
    print(median_of_medians_select(a, 0, len(a), k))