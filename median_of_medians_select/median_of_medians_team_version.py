# VERSIONE 2

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
    if high-low <= 5:
        insertion_sort(arr, low, high)
        return k-1
    else:
        z = low #NB
        counter_medians = 0

        for i in range(low, high, 5):
            if i + 5 > high: #NB
                med = median_of_medians(arr, i, high, ((high-i)//2) + i)
                arr[z], arr[med] = arr[med], arr[z]
            else:
                med = median_of_medians(arr, i, i+5, 3+i)
                arr[z], arr[med] = arr[med], arr[z]
            z += 1
            counter_medians += 1

    m = median_of_medians(arr, low, z, (counter_medians//2)+low) #indice di m
    arr[m], arr[high-1] = arr[high-1], arr[m] # scambio m con l'ultimo elemento dell'array 

    r = partition(arr, low, high)

    #chiamata ricorsiva a dx o sx a seconda del valore di k
    if r == k-1:
        return r
    elif r > k-1: # altrimenti cerco a sinistra o destra, in base alla grandezza di k
        return median_of_medians(arr, low, r, k)
    else: 
        return median_of_medians(arr, r+1, high, k)
    

if __name__ == "__main__":

    def input_array():
        return [int(x) for x in input().split(" ") if x]

    a = input_array()
    k = int(input())
    print(a[median_of_medians(a, 0, len(a), k)])