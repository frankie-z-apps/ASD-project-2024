# THIRD VERSION (ITERATIVE)

# sort the elements of arr in the interval [p,q]
def insertion_sort(arr, p, q):
    for i in range(p+1, q):
        key = arr[i]
        j = i-1
        while j >= p and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


def partition(arr, p, q, r):
    pivot = arr[r]
    arr[r], arr[q-1] = arr[q-1], arr[r]
    i = p - 1

    for j in range(p, q-1):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[q-1] = arr[q-1], arr[i+1]
    return i + 1


# return the INDEX of MEDIAN element of a sub-array arr[p,q]
def median(arr, p, q):
    insertion_sort(arr, p, q)
    median_index = (q-p) // 2
    return p+median_index   # if I return the index of median element,
                            # we can use it to switch the elements in arr, grouping all the medians together


# return the k-th smaller element in arr
def median_of_medians_select(arr, p, q, k):
    while p <= q:
        m = median_of_medians(arr, p, q)
        r = partition(arr, p, q, m)

        if r == k-1:
            return arr[r]
        elif r > k-1:
            q = r
        else:
            p = r+1
    return "Index Error!"


# return the index of median element in the sub-array arr[p,q]
def median_of_medians(arr, p, q):
    if q - p <= 5:
        return median(arr, p, q)
    else:
        med_ind = p

        for i in range(p, q, 5):
            if i + 5 <= q:
                m = median(arr, i, i+5)
            else:
                m = median(arr, i, q)
            
            arr[med_ind], arr[m] = arr[m], arr[med_ind]
            med_ind += 1
        
        return median_of_medians(arr, p, med_ind) 


if __name__ == "__main__":
        
    def input_array():
        return [int(x) for x in input().split(" ") if x]

    a = input_array()
    k = int(input())
    print(median_of_medians_select(a, 0, len(a), k))