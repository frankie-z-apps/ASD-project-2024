def input_array():
    return [int(x) for x in input().split(" ") if x]


class MinHeap:
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


    def length(self):
        return len(self.heap)
    

    def getmin(self):
        assert len(self.heap) > 0, "heap is empty"
        return self.heap[0]
    

    def extract(self):
        self.heap[0] = self.heap[-1]
        self.heap = self.heap[:-1]
        self.heapify(0)
        
    # uguale
    def insert(self, values:tuple):
        self.heap.append(values)
        self.moveup(len(self.heap)-1)
        

    def printHeap(self):
        for i in range(len(self.heap)):
            print(self.heap[i], end=" ")
        print('\n')


    def buildheap(self, array):
        self.heap = array.copy()
        for i in range(len(self.heap) // 2, -1, -1):
            self.heapify(i)
        

# assume che left(i) e right(i) siano sotto-heap valide
# modifica la heap per creare anche i come sotto-heap valida 
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


# muove i verso l'alto, fino a che l'ordine è corretto
    def moveup(self, i):
        p = self.parent(i)
        if p != None and self.heap[i][0] < self.heap[p][0]:
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            self.moveup(p)


myMinHeap = MinHeap()

def heap_select(arr, k): # complessità O(n + k log k)
    # main_heap o heap principale, creata con buildheap
    main_heap = MinHeap()
    main_heap.buildheap(arr) # tempo O(n)
    
    # aux_heap o heap ausiliaria, di coppie di interi, valore intero e posizione nella heap
    aux_heap = MinHeap()
    aux_heap.insert((main_heap.heap[0][0], 0))

    for i in range(0, k-1): # k volte
        (val, ind) = aux_heap.getmin()
        aux_heap.extract()

        # figli destro e sx che provengono dalla heap principale
        l = main_heap.left(ind)
        r = main_heap.right(ind)
        if l != None:
            aux_heap.insert( (main_heap.heap[l][0], l) )
        if r != None:
            aux_heap.insert( (main_heap.heap[r][0], r) )
    (val, ind) = aux_heap.getmin()        
    return val


'''
myMinHeap.insert((3, 0))
myMinHeap.insert((4, 0))
myMinHeap.insert((1, 0))
myMinHeap.printHeap()
print(myMinHeap.left(0))
print(myMinHeap.right(0))
print(myMinHeap.parent(1))
print(myMinHeap.getmin())
myMinHeap.extract()
myMinHeap.printHeap()
'''

def tuplefy(arr):
    tuples = []
    for i in range(len(arr)):
        tuples.append((arr[i], 0))
    return tuples
'''
arr = [11, 6, 0, 9, 3, 5, 7]
tuples = tuplefy(arr)
'''

inputArr = input_array()
k = int(input())
tuples = tuplefy(inputArr)
print(heap_select(tuples, k))