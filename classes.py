class heap(object):

    def __init__(self) -> None:
        self.queue = []
        self.size = 0

    def getParentIndex(self, index) -> int:
        return (index - 1) // 2

    def getLeftChildIndex(self, index) -> int:
        return 2 * index + 1

    def getRightChildIndex(self, index) -> int:
        return 2 * index + 2

    def hasParent(self, index) -> bool:
        return self.getParentIndex(index) >= 0

    def hasLeftChild(self, index) -> bool:
        return self.getLeftChildIndex(index) < self.size

    def hasRightChild(self, index) -> bool:
        return self.getRightChildIndex(index) < self.size

    def parent(self, index):
        return self.queue[self.getParentIndex(index)]

    def leftChild(self, index):
        return self.queue[self.getLeftChildIndex(index)]

    def rightChild(self, index):
        return self.queue[self.getRightChildIndex(index)]

    def swap(self, index1, index2):

       self.queue[index1], self.queue[index2] = self.queue[index2], self.queue[index1]

    def insert(self, data):
        self.queue.append(data)
        self.size += 1
        self.heapifyUp()

    def heapifyUp(self):
        index = self.size - 1
        
        while self.hasParent(index) and self.parent(index) < self.queue[index]:
            self.swap(self.getParentIndex(index), index)
            index = self.getParentIndex(index)


    def removeMax(self):

        data = self.queue.pop(0)
        self.queue[0] = self.queue[self.size - 1]
        self.size -= 1
        self.heapifyDown()

        return data

    def heapifyDown(self):
        
        index = 0

        while self.hasLeftChild(index):
            largerChildIndex = self.getLeftChildIndex(index)

            if self.hasRightChild(index) and self.rightChild(index) > self.leftChild(index):
                largerChildIndex = self.getRightChildIndex(index)

            if self.queue[index] > self.queue[largerChildIndex]:
                break

            else:
                self.swap(index, largerChildIndex)

            index = largerChildIndex

    def display(self):
        print(self.queue)

class JobID(object):

    def __init__(self, priority, length) -> None:
        self.priority = priority
        self.length = length

    def sliceConsume(self):
        self.length -= 1

    def __gt__(self, U):

        if self.priority > U.priority:
            return True
        else:
            return False


