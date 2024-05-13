from math import ceil

def input_array():
    return [int(x) for x in input().split(" ") if x]


def insertion_sort(arr, p, q):
    for i in range(p+1, q):
        k = arr[i]
        j = i - 1
        while(j>=p and arr[j] > k):
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = k


def partition(a, low, high):
    p = a[high-1]
    i = low
    for j in range(low, high-1):
        if a[j] <= p:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[high-1] = a[high-1], a[i]

    return i


def median_of_medians(arr, low, high, k):
    if high-low < 5:
        insertion_sort(arr, low, high)
        return arr[k-1]
    else:
        z = low
        medians_counter = 0
        # 1 - divisione dell'array in blocchi di 5 elementi
        for i in range(low, high, 5):
            # 2 - ordinamento e calcolo della mediana di ciascun blocco
            if i + 5 > high:
                insertion_sort(arr, i, high)
                arr[z], arr[ ceil((high + i)/2)-1 ] = arr[ ceil((high + i)/2)-1 ], arr[z]
            else:
                insertion_sort(arr, i, i+5)
                arr[z], arr[i+2] = arr[i+2], arr[z]

            z += 1
            medians_counter += 1
            
    # 3 - calcolo della mediana delle mediane tramite chiamata ricorsiva
    if (medians_counter % 2 == 0):
        m = median_of_medians(arr, low, z, (medians_counter//2)+low)
    else:
        m = median_of_medians(arr, low, z, ((medians_counter//2)+1)+low)
    ind = arr.index(m)
    
    arr[ind], arr[high-1] = arr[high-1], arr[ind]

    # 4 - partizionamento dell'array originario con perno la mediana delle mediane
    r = partition(arr, low, high)

    # 5 - chiamata ricorsiva a dx o sx a seconda del valore di k
    if r == k-1:
        return arr[r]
    elif r > k-1:
        return median_of_medians(arr, low, r, k)
    else: 
        return median_of_medians(arr, r+1, high, k)
    

a = input_array()
k = int(input())
print(median_of_medians(a, 0, len(a), k))
