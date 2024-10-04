# HEAP SELECT WITH MAX/MIN-HEAP - ITERATIVE VERSION

class MaxHeap:
    def __init__(self):
        # We use a list to represent the heap
        self.heap = []


    # Helper function to get the parent index
    def parent(self, index):
        return (index - 1) // 2


    # Helper function to get the left child index
    def left(self, index):
        return 2 * index + 1


    # Helper function to get the right child index
    def right(self, index):
        return 2 * index + 2


    # Swap helper function to keep the code clean
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


    # Insert an element into the heap
    def insert(self, key):
        # Add the new element to the end of the list
        self.heap.append(key)
        # Bubble it up to maintain the heap property
        self.move_up(len(self.heap) - 1)


    def move_up(self, index):
        # Bubble up the element at index until the heap property is restored
        while index > 0:
            parent = self.parent(index)
            if self.heap[index] > self.heap[parent]:
                self.swap(index, parent)
                index = parent
            else:
                break


    # Extract the maximum element (root)
    def extract_max(self):
        if len(self.heap) == 0:
            raise IndexError("extract_max(): empty heap")
        # Replace the root of the heap with the last element
        self.swap(0, len(self.heap) - 1)
        max_value = self.heap.pop()  # Remove the last element (the original root)
        # Bubble down the new root to restore heap property
        self.move_down(0)
        return max_value


    def move_down(self, index):
        size = len(self.heap)
        while index < size:
            left = self.left(index)
            right = self.right(index)
            largest = index

            # Find the largest of the current index and its children
            if left < size and self.heap[left] > self.heap[largest]:
                largest = left
            if right < size and self.heap[right] > self.heap[largest]:
                largest = right

            # If the largest is not the current index, swap and continue bubbling down
            if largest != index:
                self.swap(index, largest)
                index = largest
            else:
                break


    # Peek at the maximum element without removing it
    def peek_max(self):
        if len(self.heap) == 0:
            raise IndexError("peek_max(): empty heap")
        return self.heap[0]


    # Heapify an arbitrary list (in-place conversion)
    def heapify(self, arr):
        self.heap = arr
        # Start from the first non-leaf node and bubble down
        for i in range((len(self.heap) // 2) - 1, -1, -1):
            self.move_down(i)


    # Get the size of the heap
    def size(self):
        return len(self.heap)


    # Check if the heap is empty
    def is_empty(self):
        return len(self.heap) == 0

   

class MinHeap:
    def __init__(self):
        # We use a list to represent the heap
        self.heap = []


    # Helper function to get the parent index
    def parent(self, index):
        return (index - 1) // 2


    # Helper function to get the left child index
    def left(self, index):
        return 2 * index + 1


    # Helper function to get the right child index
    def right(self, index):
        return 2 * index + 2


    # Swap helper function to keep the code clean
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


    # Insert an element into the heap
    def insert(self, key):
        # Add the new element to the end of the list
        self.heap.append(key)
        # Bubble it up to maintain the heap property
        self.move_up(len(self.heap) - 1)


    def move_up(self, index):
        # Bubble up the element at index until the heap property is restored
        while index > 0:
            parent = self.parent(index)
            if self.heap[index] < self.heap[parent]:
                self.swap(index, parent)
                index = parent
            else:
                break


    # Extract the maximum element (root)
    def extract_min(self):
        if len(self.heap) == 0:
            raise IndexError("extract_min(): empty heap")
        # Replace the root of the heap with the last element
        self.swap(0, len(self.heap) - 1)
        min_value = self.heap.pop()  # Remove the last element (the original root)
        # Bubble down the new root to restore heap property
        self.move_down(0)
        return min_value


    def move_down(self, index):
        size = len(self.heap)
        while index < size:
            left = self.left(index)
            right = self.right(index)
            smallest = index

            # Find the smallest of the current index and its children
            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right

            # If the smallest is not the current index, swap and continue bubbling down
            if smallest != index:
                self.swap(index, smallest)
                index = smallest
            else:
                break


    # Peek at the minimum element without removing it
    def peek_min(self):
        if len(self.heap) == 0:
            raise IndexError("peek_min(): empty heap")
        return self.heap[0]


    # Heapify an arbitrary list (in-place conversion)
    def heapify(self, arr):
        self.heap = arr
        # Start from the first non-leaf node and bubble down
        for i in range((len(self.heap) // 2) - 1, -1, -1):
            self.move_down(i)


    # Get the size of the heap
    def size(self):
        return len(self.heap)


    # Check if the heap is empty
    def is_empty(self):
        return len(self.heap) == 0


'''
    Representation of an auxiliary Min-Heap in which elements are pairs of the form [value, index].
    The heap position of each element is based on its 'value' field.
'''
class AuxMinHeap(MinHeap):
    def aux_min_move_down(self, index):
        size = len(self.heap)
        while index < size:
            left = self.left(index)
            right = self.right(index)
            smallest = index


            # Find the smallest of the current index and its children
            if left < size and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left
            if right < size and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right


            # If the largest is not the current index, swap and continue bubbling down
            if smallest != index:
                self.swap(index, smallest)
                index = smallest
            else:
                break
    

    def aux_min_move_up(self, index):
        # Bubble up the element at index until the heap property is restored
        while index > 0:
            parent = self.parent(index)
            if self.heap[index][0] < self.heap[parent][0]:
                self.swap(index, parent)
                index = parent
            else:
                break


'''
    Representation of an auxiliary Max-Heap in which elements are pairs of the form [value, index].
    The heap position of each element is based on its 'value' field.
'''
class AuxMaxHeap(MaxHeap):
    def aux_max_move_down(self, index):
        size = len(self.heap)
        while index < size:
            left = self.left(index)
            right = self.right(index)
            largest = index


            # Find the largest of the current index and its children
            if left < size and self.heap[left][0] > self.heap[largest][0]:
                largest = left
            if right < size and self.heap[right][0] > self.heap[largest][0]:
                largest = right


            # If the largest is not the current index, swap and continue bubbling down
            if largest != index:
                self.swap(index, largest)
                index = largest
            else:
                break
    

    def aux_max_move_up(self, index):
        # Bubble up the element at index until the heap property is restored
        while index > 0:
            parent = self.parent(index)
            if self.heap[index][0] > self.heap[parent][0]:
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


def select_max_heap(arr, start, end, k):
    main_heap = MaxHeap()
    aux_heap = AuxMaxHeap()
    main_heap.heapify(arr)
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


def select_min_heap(arr, start, end, k):
    main_heap = MinHeap()
    aux_heap = AuxMinHeap()
    main_heap.heapify(arr)
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