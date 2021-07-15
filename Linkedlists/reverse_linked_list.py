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

    def reverse_list(self):
        prev = None
        curr = self.head
        while curr:
            next_1 = curr.next
            curr.next = prev
            prev = curr
            curr = next_1
        self.head = prev


if __name__ == '__main__':
    obj = LinkedList()
    obj.insert_at_end(50)
    obj.insert_at_end(60)
    obj.insert_at_end(70)
    obj.insert_at_end(80)
    obj.print_list()
    obj.reverse_list()
    obj.print_list()
