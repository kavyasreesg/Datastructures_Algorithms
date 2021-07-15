class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()

    def mid_ele_ll(self):
        if self.head is None:
            print("Empty list")
            return
        ptr1 = self.head
        ptr2 = self.head
        while ptr2.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
        return ptr1.data


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_end(10)
    ll.insert_end(20)
    ll.insert_end(30)
    ll.insert_end(40)
    ll.insert_end(50)
    ll.print_list()
    print(ll.mid_ele_ll())
