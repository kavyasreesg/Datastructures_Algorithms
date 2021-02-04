class MaxHeap:

    def __init__(self, items=[]):
        self.heap = [0]
        for item in items:
            self.heap.append(item)
            self.__float_up(len(self.heap) - 1)

    def push(self, data):
        self.heap.append(data)
        self.__float_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max_ele = self.heap.pop()
            self.__bubble_down(1)
        elif len(self.heap) == 2:
            max_ele = self.heap.pop()
        else:
            max_ele = False
        return max_ele

    def peek(self):
        if len(self.heap) > 0:
            return self.heap[1]
        else:
            return False

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __float_up(self, index):
        parent = index // 2
        if index <= 1:
            return
        elif self.heap[parent] < self.heap[index]:
            self.__swap(index, parent)
            self.__float_up(parent)

    def __bubble_down(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(largest, index)
            self.__bubble_down(largest)

    def __str__(self):
        return str(self.heap[1:])


if __name__ == "__main__":
    heap_obj = MaxHeap([95, 3, 21])
    heap_obj.push(10)
    heap_obj.push(20)
    heap_obj.pop()
    peeked_ele = heap_obj.peek()
    print(peeked_ele)
    print(heap_obj)
