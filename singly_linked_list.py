class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return '(' + str(self.data) + ')'


class LinkedList:

    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1

    def find(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                return d
            else:
                this_node = this_node.next_node
        return None

    def remove(self, d):
        prev_node = None
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                if prev_node is not None:
                    prev_node.next_node = this_node.next_node
                else:
                    self.root = this_node.next_node
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.next_node
        return False

    def print_linked_list(self):
        this_node = self.root
        while this_node is not None:
            print(this_node, end='->')
            this_node = this_node.next_node


if __name__ == "__main__":
    linked_list1 = LinkedList()
    for i in range(5):
        linked_list1.add(i)
    linked_list1.remove(0)
    d = linked_list1.find(2)
    if d:
        print("Element {} is present in linked list".format(d))
    else:
        print("Element is not present in linked list")
    print(linked_list1.print_linked_list())
