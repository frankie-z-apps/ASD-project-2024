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


if __name__ == "__main__":
    
    def input_array():
        return [int(x) for x in input().split(" ") if x]

    arr = input_array()
    k = int(input())
    print(heap_select(arr, k))