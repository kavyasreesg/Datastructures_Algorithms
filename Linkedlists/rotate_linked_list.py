class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):  # O(N)
        if self.head is None:
            self.head = Node(data, None)
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        node = Node(data)
        temp.next = node

    def print_list(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp = self.head
            while temp:
                print("{} ".format(temp.data), end='')
                temp = temp.next
        print()

    def rotate(self, k):
        temp = self.head
        length = 1
        while temp.next:
            length += 1
            temp = temp.next
        temp.next = self.head
        curr = self.head
        k = k % length
        rem = length - k
        print(temp.next.data)
        while rem > 1:
            curr = curr.next
            rem -= 1
        self.head = curr.next
        curr.next = None


if __name__ == '__main__':
    obj = LinkedList()
    obj.insert_at_end(1)
    obj.insert_at_end(2)
    obj.insert_at_end(3)
    obj.insert_at_end(4)
    obj.insert_at_end(5)
    obj.rotate(2)
    obj.print_list()

