# LAB ES3

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
            #scambio a[i] con a[j]
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[high-1] = a[high-1], a[i]

    return i


def median_of_medians(arr, low, high, k):
    if high-low < 5:
        insertion_sort(arr, low, high)
        return arr[k-1]
    else:
        z = low #NB
        counter_medians = 0

        for i in range(low, high, 5):

            if i + 5 > high: #NB
                insertion_sort(arr, i, high)
                # print(f"mediano dell'ultimo blocco: {arr[(len(arr) + i)//2]}")
                arr[z], arr[ ceil((high + i)/2)-1 ] = arr[ ceil((high + i)/2)-1 ], arr[z] #NB
            else:
                insertion_sort(arr, i, i+5)
                arr[z], arr[i+2] = arr[i+2], arr[z]

            z += 1
            counter_medians += 1
            
        
    # versione ricorsiva:
    if (counter_medians % 2 == 0): #NB
        m = median_of_medians(arr, low, z, (counter_medians//2)+low)
    else:
        m = median_of_medians(arr, low, z, ((counter_medians//2)+1)+low)
    ind = arr.index(m)
    
    arr[ind], arr[high-1] = arr[high-1], arr[ind] # scambio m con l'ultimo elemento dell'array 

    # 4 - partizionamento dell'array originario con perno la mediana delle mediane
    
    r = partition(arr, low, high)
    #print(f"median of medians: {m}")
    #print(f"array: {arr}")
    #print(f"partition(array): {arr[r]}")

    # 5 - chiamata ricorsiva a dx o sx a seconda del valore di k
    if r == k-1:
        return arr[r]
    elif r > k-1: # altrimenti cerco a sinistra o destra, in base alla grandezza di k
        return median_of_medians(arr, low, r, k)
    else: 
        return median_of_medians(arr, r+1, high, k)
    

#a = input_array()
#k = int(input())
#print(median_of_medians(a, 0, len(a), k))


#PROVE

myarr = [25, 12, 8, 9, 3, 7, 52, 10, -2, 24, 5, 29, 59, 23]
myarr2 = [12, 32, 5, 6, 3, 69]
myarr3 = [9, -2, 7, 8, 5, 3, 10, 12, 23, 29, 52, 59, 24, 25]
#myarr-sorted = [-2, 3, 5, 7, 8, 9, 10, 12, 23, 24, 25, 29, 52, 59]
#myarr2-sorted = [3, 5, 6, 12, 32, 69]

print(median_of_medians(myarr, 0, len(myarr), 1))
print(median_of_medians(myarr2, 0, len(myarr2), 2))
print(median_of_medians(myarr3, 0, len(myarr3), 5))
