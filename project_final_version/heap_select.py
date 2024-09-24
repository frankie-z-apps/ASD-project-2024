# HEAP SELECT WITH MAX/MIN-HEAP 


'''
    Representation of Heap data structure
    and methods valid for both max and min-heaps
'''
class Heap:
    heap = []


    # return left leaf of element i, if existing
    def left(self, i):
        j = 2*i + 1
        if j >= len(self.heap):
            return None
        else:
            return j


    # return right leaf of element i, if existing
    def right(self, i):
        j = 2*i + 2
        if j >= len(self.heap):
            return None
        else:
            return j


    # return parent of element i, if existing
    def parent(self, i):
        if i == 0:
            return None
        return (i+1) // 2 - 1
    

    # return first element of heap, if heap is non-empty
    def peek(self):
        assert len(self.heap) > 0, "heap is empty"
        return self.heap[0]


    # print elements of heap
    def printHeap(self):
        for i in range(len(self.heap)):
            print(self.heap[i], end=" ")
        print('\n')
    

'''
    Representation of Min-Heap data structure
'''
class MinHeap(Heap):
    # remove first element of Min-Heap (min value)
    def extract(self):
        self.heap[0] = self.heap[-1]
        self.heap = self.heap[:-1]
        self.heapify(0)


    # transform array in a Min-Heap
    def build_heap(self, array):
        self.heap = array.copy()
        for i in range(len(self.heap) // 2, -1, -1):
            self.heapify(i)
        

    # put element at index i in its correct place,
    # keeping the structure a valid Min-Heap
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

    
    # insert value in Min-Heap and put it in its place, 
    # keeping the structure a valid Min-Heap
    def insert(self, value):
        self.heap.append(value)
        self.move_up(len(self.heap)-1)


    # move up element at index i until it is in its correct place
    def move_up(self, i):
        p = self.parent(i)
        if p != None and self.heap[i] < self.heap[p]:
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            self.move_up(p)


'''
    Representation of Max-Heap data structure
'''
class MaxHeap(Heap):
    # remove first element of Max-Heap (max value)
    def extract(self):
        self.heap[0] = self.heap[-1]
        self.heap = self.heap[:-1]
        self.heapify(0)


    # transform array in a Max-Heap
    def build_heap(self, array):
        self.heap = array.copy()
        for i in range(len(self.heap) // 2, -1, -1):
            self.heapify(i)
        
    
    # put element at index i in its correct place,
    # keeping the structure a valid Max-Heap
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

    
    # insert value in Max-Heap and put it in its place, 
    # keeping the structure a valid Max-Heap
    def insert(self, value):
        self.heap.append(value)
        self.move_up(len(self.heap)-1)

    
    # move up element at index i until it is in its correct place
    def move_up(self, i):
        p = self.parent(i)
        if p != None and self.heap[i] > self.heap[p]:
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            self.move_up(p)


'''
    Representation of an auxiliary Min-Heap in which elements are pairs of the form [value, index].
    The heap position of each element is based on its 'value' field.
'''
class AuxMinHeap(MinHeap):
    # put element at index i in its correct place, 
    # keeping the structure a valid auxiliary Min-Heap 
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
    

    # move up element at index i until it is in its correct place
    def move_up(self, i):
        p = self.parent(i)
        if p != None and self.heap[i][0] < self.heap[p][0]:
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            self.move_up(p)


'''
    Representation of an auxiliary Max-Heap in which elements are pairs of the form [value, index].
    The heap position of each element is based on its 'value' field.
'''
class AuxMaxHeap(MaxHeap):   
    # put element at index i in its correct place, 
    # keeping the structure a valid auxiliary Max-Heap 
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
    

    # move up element at index i until it is in its correct place
    def move_up(self, i):
        p = self.parent(i)
        if p != None and self.heap[i][0] > self.heap[p][0]:
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            self.move_up(p)



'''
    Return the k-th smallest element in arr (without sorting it) 
    making use of the heap data structure.
    Input array is transformed into a Max-Heap or Min-Heap depending on the value of k. 
'''
def heap_select(arr, start, end, k):
    if k > len(arr)//2:
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


'''
    Return the k-th smallest element in arr (without sorting it) 
    making use of the Min-Heap data structure.
'''
def min_heap_select(arr, p, q, k):
    main_heap = MinHeap()
    main_heap.build_heap(arr)
    
    aux_heap = AuxMinHeap()
    aux_heap.insert((main_heap.heap[0], 0))

    for i in range(0, k-1):
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
    print(heap_select(arr, None, None, k))