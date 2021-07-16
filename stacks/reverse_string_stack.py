from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, data):
        self.container.append(data)

    def push_elements(self, array):
        for ele in array:
            self.push(ele)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


s = Stack()
s.push_elements("Kavyasree is a good girl")
array1 = []
for i in range(s.size()):
    array1.append(s.pop())
print(''.join(array1))

