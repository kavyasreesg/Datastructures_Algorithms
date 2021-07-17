from collections import deque
import threading
import time


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


def place_order(list_1):
    for ele in list_1:
        print("Placing order for: ",ele)
        q.enqueue(ele)
        time.sleep(0.5)


def serve_order():
    time.sleep(1)
    while not q.is_empty():
        order = q.dequeue()
        print("Now serving ",order)
        time.sleep(2)


inp = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
t1 = threading.Thread(target=place_order, args=(inp,))
t2 = threading.Thread(target=serve_order)
t1.start()
t2.start()
