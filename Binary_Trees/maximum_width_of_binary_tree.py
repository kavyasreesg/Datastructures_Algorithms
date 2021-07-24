import sys

"""
Maximum width is achieved by performing level order traversal (bfs)
Initialize queue with root
Use queue to add elements in each level
pop each element in queue and add it's right and left children if present
calculate count of queue each time and store max and return the maximum
That gives the maximum of nodes
"""


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinaryTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinaryTreeNode(data)


def max_width(root):
    queue = [root]
    maximum = -sys.maxsize
    while queue:
        element = queue.pop(0)
        if element.left:
            queue.append(element.left)
        if element.right:
            queue.append(element.right)
        maximum = max(len(queue), maximum)
    return maximum


def build_tree(elements):
    root = BinaryTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root


if __name__ == '__main__':
    # You can also use strings in list
    list_of_inputs = [15, 12, 14, 7, 20, 27, 88, 23]
    node = build_tree(list_of_inputs)
    max_width_nodes = max_width(node)
    print(max_width_nodes)
