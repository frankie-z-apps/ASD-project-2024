# HEAP SELECT WITH MAX/MIN-HEAP - ITERATIVE VERSION

class MaxHeap:
    def __init__(self):
        self.heap = []


    '''
        Get parent index
    '''
    def parent(self, index):
        return (index - 1) // 2


    '''
        Get left child index
    '''
    def left(self, index):
        return 2 * index + 1


    '''
        Get right child index
    '''
    def right(self, index):
        return 2 * index + 2


    '''
        Swap elements of index i and j
    '''
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


    '''
        Insert new element into MaxHeap
    '''
    def insert(self, key):
        self.heap.append(key)
        self.move_up(self.size() - 1)


    '''
        Move up the element at index until heap property is restored
    '''
    def move_up(self, index):
        while index > 0:
            parent = self.parent(index)

            if self.heap[index] > self.heap[parent]:
                self.swap(index, parent)
                index = parent
            else:
                break


    '''
        Extract max element (root)
    '''
    def extract_max(self):
        if self.is_empty():
            raise IndexError("extract_max(): empty heap")
        self.swap(0, self.size() - 1)
        max_value = self.heap.pop()
        self.heapify(0)
        return max_value

    '''
        Move down element at index until heap property is restored
    '''
    def heapify(self, index):
        size = self.size()

        while index < size:
            left = self.left(index)
            right = self.right(index)
            largest = index

            if left < size and self.heap[left] > self.heap[largest]:
                largest = left
            if right < size and self.heap[right] > self.heap[largest]:
                largest = right

            if largest != index:
                self.swap(index, largest)
                index = largest
            else:
                break


    '''
        Peek at max element (root) without removing it
    '''
    def peek_max(self):
        if self.is_empty():
            raise IndexError("peek_max(): empty heap")
        return self.heap[0]


    '''
        Build a MaxHeap starting from a generic array
    '''
    def build_heap(self, arr):
        self.heap = arr
        for i in range((self.size() // 2) - 1, -1, -1):
            self.heapify(i)


    '''
        Get heap size
    '''
    def size(self):
        return len(self.heap)


    '''
        Check if heap is empty
    '''
    def is_empty(self):
        return self.size() == 0

   

class MinHeap:
    def __init__(self):
        self.heap = []


    '''
        Get parent index
    '''
    def parent(self, index):
        return (index - 1) // 2


    '''
        Get left child index
    '''
    def left(self, index):
        return 2 * index + 1


    '''
        Get right child index
    '''
    def right(self, index):
        return 2 * index + 2


    '''
        Swap elements of index i and j
    '''
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


    '''
        Insert new element into MaxHeap
    '''
    def insert(self, key):
        self.heap.append(key)
        self.move_up(self.size() - 1)


    '''
        Move up the element at index until heap property is restored
    '''
    def move_up(self, index):
        while index > 0:
            parent = self.parent(index)

            if self.heap[index] < self.heap[parent]:
                self.swap(index, parent)
                index = parent
            else:
                break


    '''
        Extract min element (root)
    '''
    def extract_min(self):
        if self.is_empty():
            raise IndexError("extract_min(): empty heap")
        self.swap(0, self.size() - 1)
        min_value = self.heap.pop()
        self.heapify(0)
        return min_value


    '''
        Move down element at index until heap property is restored
    '''
    def heapify(self, index):
        size = self.size()

        while index < size:
            left = self.left(index)
            right = self.right(index)
            smallest = index

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != index:
                self.swap(index, smallest)
                index = smallest
            else:
                break


    '''
        Peek at min element (root) without removing it
    '''
    def peek_min(self):
        if self.is_empty():
            raise IndexError("peek_min(): empty heap")
        return self.heap[0]


    '''
        Build a MinHeap starting from a generic array
    '''
    def build_heap(self, arr):
        self.heap = arr
        for i in range((self.size() // 2) - 1, -1, -1):
            self.heapify(i)


    '''
        Get heap size
    '''
    def size(self):
        return len(self.heap)


    '''
        Check if heap is empty
    '''
    def is_empty(self):
        return self.size() == 0


'''
    Representation of an auxiliary Max-Heap in which elements are pairs of the form [value, index].
    The heap position of each element is based on its 'value' field.
'''
class AuxMaxHeap(MaxHeap):
    '''
        Move down element at index until heap property is restored
    '''
    def aux_max_heapify(self, index):
        size = self.size()
        while index < size:
            left = self.left(index)
            right = self.right(index)
            largest = index
            
            if left < size and self.heap[left][0] > self.heap[largest][0]:
                largest = left
            if right < size and self.heap[right][0] > self.heap[largest][0]:
                largest = right

            if largest != index:
                self.swap(index, largest)
                index = largest
            else:
                break
    

    '''
        Move up element at index until heap property is restored
    '''
    def aux_max_move_up(self, index):
        while index > 0:
            parent = self.parent(index)

            if self.heap[index][0] > self.heap[parent][0]:
                self.swap(index, parent)
                index = parent
            else:
                break



'''
    Representation of an auxiliary Min-Heap in which elements are pairs of the form [value, index].
    The heap position of each element is based on its 'value' field.
'''
class AuxMinHeap(MinHeap):
    '''
        Move down element at index until heap property is restored
    '''
    def aux_min_heapify(self, index):
        size = self.size()
        while index < size:
            left = self.left(index)
            right = self.right(index)
            smallest = index

            if left < size and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left
            if right < size and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right
            
            if smallest != index:
                self.swap(index, smallest)
                index = smallest
            else:
                break
    

    '''
        Move up element at index until heap property is restored
    '''
    def aux_min_move_up(self, index):
        while index > 0:
            parent = self.parent(index)
     
            if self.heap[index][0] < self.heap[parent][0]:
                self.swap(index, parent)
                index = parent
            else:
                break


'''
    Return the k-th smallest element in arr (without sorting it) 
    making use of the heap data structure.
    Input array is transformed into a Max-Heap or Min-Heap depending on the value of k. 
'''
def heap_select(arr, start, end, k):
    if k > len(arr)//2:
        return select_max_heap(arr, None, None, k)
    else:
        return select_min_heap(arr, None, None, k)


'''
    Execute algorithm using a MaxHeap
'''
def select_max_heap(arr, start, end, k):
    main_heap = MaxHeap()
    aux_heap = AuxMaxHeap()
    main_heap.build_heap(arr)
    aux_heap.insert((main_heap.heap[0], 0))

    for i in range(len(arr) - k):
        (val, ind) = aux_heap.peek_max()
        aux_heap.extract_max()

        l = main_heap.left(ind)
        r = main_heap.right(ind)
        if l < len(arr):
            aux_heap.insert((main_heap.heap[l], l))
        if r < len(arr):
            aux_heap.insert((main_heap.heap[r], r))
    (val, ind) = aux_heap.peek_max()
    return val


'''
    Execute algorithm using a MinHeap
'''
def select_min_heap(arr, start, end, k):
    main_heap = MinHeap()
    aux_heap = AuxMinHeap()
    main_heap.build_heap(arr)
    aux_heap.insert((main_heap.heap[0], 0))

    for i in range(k-1):
        (val, ind) = aux_heap.peek_min()
        aux_heap.extract_min()

        l = main_heap.left(ind)
        r = main_heap.right(ind)
        if l < len(arr):
            aux_heap.insert((main_heap.heap[l], l))
        if r < len(arr):
            aux_heap.insert((main_heap.heap[r], r))
    (val, ind) = aux_heap.peek_min()
    return val


if __name__ == "__main__":
    
    def input_array():
        return [int(x) for x in input().split(" ") if x]

    arr = input_array()
    k = int(input())
    print(heap_select(arr, None, None, k))