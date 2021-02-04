class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return '(' + str(self.data) + ')'


class CircularLinkedList:

    def __init__(self, root=None):
        self.root = root
        self.size = 0

    # Inserting as second node in the linked list
    # eg : root -> 1 -> 2 -> root
    def add(self, d):
        if self.size == 0:
            self.root = Node(d)
            self.root.next_node = self.root
        else:
            new_node = Node(d, self.root.next_node)
            self.root.next_node = new_node
        self.size += 1

    def find(self, d):
        this_node = self.root
        while True:
            if this_node.data == d:
                return d
            elif this_node.next_node == self.root:
                return False
            this_node = this_node.next_node

    def remove(self, d):
        this_node = self.root
        prev_node = None

        while True:
            if this_node.data == d:
                if prev_node is not None:
                    prev_node.next_node = this_node.next_node
                else:
                    while this_node.next_node != self.root:
                        this_node = this_node.next_node
                    this_node.next_node = self.root.next_node
                    self.root = self.root.next_node
                self.size -= 1
                return True

            elif this_node.next_node == self.root:
                return False
            prev_node = this_node
            this_node = this_node.next_node

    def print_circular_linked_list(self):
        if self.root is None:
            return
        this_node = self.root
        print(this_node, end='->')
        while this_node.next_node != self.root:
            this_node = this_node.next_node
            print(this_node, end='->')
        print(self.root)  # Printing again the root Node (since it is
        # circular linked list


if __name__ == "__main__":
    circular_ll_obj = CircularLinkedList()
    for i in range(1, 5):
        circular_ll_obj.add(i)
    circular_ll_obj.remove(1)  # Removing root node
    print(circular_ll_obj.print_circular_linked_list())
    data_search = circular_ll_obj.find(2)
    if data_search:
        print("Element {} found in circular linked list".format(data_search))
