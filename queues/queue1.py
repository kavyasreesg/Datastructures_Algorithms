from collections import deque


class Queue:
    def __init__(self):
        self.container = deque()

    def enqueue(self, data):
        self.container.appendleft(data)

    def dequeue(self):
        return self.container.pop()

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


q = Queue()
q.enqueue({
    'company': 'walmart',
    'timestamp': '15 apr, 11 01 AM',
    'price': 132
})
q.enqueue({
    'company': 'walmart',
    'timestamp': '15 apr, 11 03 AM',
    'price': 133.5
})
q.enqueue({
    'company': 'walmart',
    'timestamp': '15 apr, 11 05 AM',
    'price': 134
})
print(q.container)
print(q.size())
print(q.dequeue())
