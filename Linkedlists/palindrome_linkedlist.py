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

    def is_palindrome(self):
        curr = self.head
        fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            curr = curr.next
        prev = None
        while curr:
            next_1 = curr.next
            curr.next = prev
            prev = curr
            curr = next_1
        left, right = self.head, prev
        while right:
            if left.data != right.data:
                return False
            left = left.next
            right = right.next
        return True


if __name__ == '__main__':
    obj = LinkedList()
    obj.insert_at_end(1)
    obj.insert_at_end(2)
    obj.insert_at_end(2)
    obj.insert_at_end(1)
    obj.print_list()
    print(obj.is_palindrome())
