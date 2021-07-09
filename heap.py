# so we are going to learn how to implement heap

class Heap(object):
    heap_size = 10

    def __init__(self):
        self.heap = [0]*Heap.heap_size
        self.currentPos = -1

    def insert(self, item):

        if self.isFull():
            print("heap is already full, consider deleting something")
            return
        self.currentPos = self.currentPos + 1
        self.heap[self.currentPos] = item
        self.fixup(self.currentPos)

    def fixup(self , index):
        parent_index = int((index-1)/2)
        while parent_index >= 0 and self.heap[index] > self.heap[parent_index]:
            temp = self.heap[index]
            self.heap[index] = self.heap[parent_index]
            self.heap[parent_index] = temp
            parent_index = int((index-1)/2)

    def isFull(self):
        if self.currentPos == Heap.heap_size:
            return True
        return False


    heap1 = Heap()
    heap1.insert(10)