from math import ceil

# QUICK SELECT

def quick_select(a, low, high, k): #intervallo a[low, ..., high-1], k = k-esimo elemento piu piccolo di a
    if (high - low < 1) or ( k-1<low or k-1>high-1 ): #se non ho neanche un elemento o k non appartiene a[low...high-1] --> errore
        return "Errore"                      
    r = partition(a, low, high)
    if r == k-1: #se a[r] = k-1 ho finito
        return a[r]
    elif r > k-1: #altrimenti cerco a sinistra o destra, in base alla grandezza di k
        return quick_select(a, low, r, k)
    else: 
        return quick_select(a, r+1, high, k)

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


# HEAP SELECT

class Heap:
    heap = []

    def left(self, i):
        j = 2*i + 1
        if j >= len(self.heap):
            return None
        else:
            return j


    def right(self, i):
        j = 2*i + 2
        if j >= len(self.heap):
            return None
        else:
            return j


    def parent(self, i):
        if i == 0:
            return None
        return (i+1) // 2 - 1
    

    def peek(self):
        assert len(self.heap) > 0, "heap is empty"
        return self.heap[0]


    def printHeap(self):
        for i in range(len(self.heap)):
            print(self.heap[i], end=" ")
        print('\n')
    

class MinHeap(Heap):
    def extract(self):
        self.heap[0] = self.heap[-1]
        self.heap = self.heap[:-1]
        self.heapify(0)


    def build_heap(self, array):
        self.heap = array.copy()
        for i in range(len(self.heap) // 2, -1, -1):
            self.heapify(i)
        

    def heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        min = i
        if l != None and self.heap[l] < self.heap[min]:
            min = l
        if r != None and self.heap[r] < self.heap[min]:
            min = r
        if min != i:
            self.heap[i], self.heap[min] = self.heap[min], self.heap[i]
            self.heapify(min)

    
    def insert(self, value):
        self.heap.append(value)
        self.move_up(len(self.heap)-1)


    def move_up(self, i):
        p = self.parent(i)
        if p != None and self.heap[i] < self.heap[p]:
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            self.move_up(p)


class MaxHeap(Heap):
    def extract(self):
        self.heap[0] = self.heap[-1]
        self.heap = self.heap[:-1]
        self.heapify(0)


    def build_heap(self, array):
        self.heap = array.copy()
        for i in range(len(self.heap) // 2, -1, -1):
            self.heapify(i)
        
    
    def heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        max = i
        if l != None and self.heap[l] > self.heap[max]:
            max = l
        if r != None and self.heap[r] > self.heap[max]:
            max = r
        if max != i:
            self.heap[i], self.heap[max] = self.heap[max], self.heap[i]
            self.heapify(max)

    
    def insert(self, value):
        self.heap.append(value)
        self.move_up(len(self.heap)-1)

    
    def move_up(self, i):
        p = self.parent(i)
        if p != None and self.heap[i] > self.heap[p]:
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            self.move_up(p)


# min-Heap che gestisce elementi formati da coppie (valore, indice)
class AuxMinHeap(MinHeap):
    def heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        min = i
        if l != None and self.heap[l][0] < self.heap[min][0]:
            min = l
        if r != None and self.heap[r][0] < self.heap[min][0]:
            min = r
        if min != i:
            self.heap[i], self.heap[min] = self.heap[min], self.heap[i]
            self.heapify(min)
    

    def move_up(self, i):
        p = self.parent(i)
        if p != None and self.heap[i][0] < self.heap[p][0]:
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            self.move_up(p)


# max-Heap che gestisce elementi formati da coppie (valore, indice)
class AuxMaxHeap(MaxHeap):
    def heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        max = i
        if l != None and self.heap[l][0] > self.heap[max][0]:
            max = l
        if r != None and self.heap[r][0] > self.heap[max][0]:
            max = r
        if max != i:
            self.heap[i], self.heap[max] = self.heap[max], self.heap[i]
            self.heapify(max)
    

    def move_up(self, i):
        p = self.parent(i)
        if p != None and self.heap[i][0] > self.heap[p][0]:
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            self.move_up(p)


def heap_select(arr, low, high, k): # complessità O(n + k log k)
    # a seconda del valore di k, lavoro con max-Heap o min-Heap
    if k > len(arr)//2:
        # a seconda che utilizzi max-Heap o min-Heap cambia il numero di iterazioni per trovare 
        # il k-1 esimo elemento
        pos = len(arr) - k
        main_heap = MaxHeap()
        aux_heap = AuxMaxHeap()
    else:
        pos = k-1
        main_heap = MinHeap()
        aux_heap = AuxMinHeap()
    
    main_heap.build_heap(arr)
    aux_heap.insert((main_heap.heap[0], 0))

    for i in range(0, pos):
        (val, ind) = aux_heap.peek()
        aux_heap.extract()

        l = main_heap.left(ind)
        r = main_heap.right(ind)
        if l != None:
            aux_heap.insert( (main_heap.heap[l], l) )
        if r != None:
            aux_heap.insert( (main_heap.heap[r], r) )
    (val, ind) = aux_heap.peek()        
    return val


# MEDIAN OF MEDIANS SELECT 

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
            if i + 5 <= high:
                insertion_sort(arr, i, i+5)
                arr[z], arr[i+2] = arr[i+2], arr[z]
            else:
                insertion_sort(arr, i, high)
                arr[z], arr[ ceil((high + i)/2)-1 ] = arr[ ceil((high + i)/2)-1 ], arr[z]                

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
    