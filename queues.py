from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()
        self.size = 0

    def enqueue(self, item):
        self.queue.append(item)
        self.size = self.size + 1

    def dequeue(self):
        if self.size > 0:
            return self.queue.popleft()
        else:
            return None

    def peek(self):
        if self.size > 0:
            ret_val = deque[0]
            return ret_val
        else:
            return None

    def get_queue_size(self):
        return self.size

    def display_queue(self):
        for ele in self.queue:
            print(ele)


if __name__ == "__main__":
    que_obj = Queue()
    que_obj.enqueue(10)
    que_obj.enqueue(20)
    que_obj.display_queue()