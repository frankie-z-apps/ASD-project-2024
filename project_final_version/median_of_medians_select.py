# MEDIAN OF MEDIANS SELECT


# sort the elements of arr in the interval [start,end]
def insertion_sort(arr, start, end):
    for i in range(start+1, end):
        key = arr[i]
        j = i-1
        while j >= start and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


# return 
def partition_r(arr, start, end, r):
    pivot = arr[r]
    arr[r], arr[end-1] = arr[end-1], arr[r]
    i = start - 1

    for j in range(start, end-1):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[end-1] = arr[end-1], arr[i+1]
    return i + 1


# return the INDEX of MEDIAN element of a sub-array arr[start,end]
def median(arr, start, end):
    insertion_sort(arr, start, end)
    median_index = (end-start) // 2
    return start+median_index   # if I return the index of median element,
                            # we can use it to switch the elements in arr, grouping all the medians together


# return the k-th smaller element in arr
def median_of_medians_select(arr, start, end, k):
    while start <= end:
        m = median_of_medians(arr, start, end)
        r = partition_r(arr, start, end, m)

        if r == k-1:
            return arr[r]
        elif r > k-1:
            end = r
        else:
            start = r+1
    print("Index Error!")


# return the index of median element in the sub-array arr[start,end]
def median_of_medians(arr, start, end):
    if end - start <= 5:
        return median(arr, start, end)
    else:
        med_ind = start

        for i in range(start, end, 5):
            if i + 5 <= end:
                m = median(arr, i, i+5)
            else:
                m = median(arr, i, end)
            
            arr[med_ind], arr[m] = arr[m], arr[med_ind]
            med_ind += 1
        
        return median_of_medians(arr, start, med_ind) 


if __name__ == "__main__":
        
    def input_array():
        return [int(x) for x in input().split(" ") if x]

    a = input_array()
    k = int(input())
    print(median_of_medians_select(a, 0, len(a), k))