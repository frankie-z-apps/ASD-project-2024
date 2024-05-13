#ALGORITMO 1 QUICKSELECT

def input_array():
    return [int(x) for x in input().split(" ") if x]

def quickselect(a, low, high, k): #intervallo a[low, ..., high-1], k = k-esimo elemento piu piccolo di a
    if (high - low < 1) or ( k-1<low or k-1>high-1 ): #se non ho neanche un elemento o k non appartiene a[low...high-1] --> errore
        return "Errore"                      
    r = partition(a, low, high)
    if r == k-1: #se a[r] = k-1 ho finito
        return a[r]
    elif r > k-1: #altrimenti cerco a sinistra o destra, in base alla grandezza di k
        return quickselect(a, low, r, k)
    else: 
        return quickselect(a, r+1, high, k)

def partition(a, low, high):
    p = a[high-1]
    i = low
    for j in range(low, high-1):
        if a[j] <= p:
            #scambio a[i] con a[j]
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[high-1] = a[high-1], a[i]

    return i #i Ã¨ la posizione da restituire!

a = input_array()
k = int(input())
print(quickselect(a, 0, len(a), k))