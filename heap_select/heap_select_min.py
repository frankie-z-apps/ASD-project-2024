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
        

    def insert(self, value):
        self.heap.append(value)
        self.moveup(len(self.heap)-1)
        
    
    def printHeap(self):
        for i in range(len(self.heap)):
            print(self.heap[i], end=" ")
        print('\n')

    
    def buildheap(self, array):
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


    def moveup(self, i):
        p = self.parent(i)
        if p != None and self.heap[i] < self.heap[p]:
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            self.moveup(p)


# min heap che gestisce elementi formati da coppie (valore, indice)
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
    

    def moveup(self, i):
        p = self.parent(i)
        if p != None and self.heap[i][0] < self.heap[p][0]:
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            self.moveup(p)


def heap_select(arr, p, q, k): # complessità O(n + k log k)
    main_heap = MinHeap()
    main_heap.buildheap(arr)
    
    aux_heap = AuxMinHeap()
    aux_heap.insert((main_heap.heap[0], 0))

    for i in range(0, k-1):
        (val, ind) = aux_heap.getmin()
        aux_heap.extract()


        l = main_heap.left(ind)
        r = main_heap.right(ind)
        if l != None:
            aux_heap.insert( (main_heap.heap[l], l) )
        if r != None:
            aux_heap.insert( (main_heap.heap[r], r) )
    (val, ind) = aux_heap.getmin()        
    return val


if __name__ == "__main__":

    inputArr = input_array()
    k = int(input())
    print(heap_select(inputArr, k))