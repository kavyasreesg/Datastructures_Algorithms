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

    def inorder_traversal(self):
        ele = []
        if self.left:
            ele += self.left.inorder_traversal()
        ele.append(self.data)
        if self.right:
            ele += self.right.inorder_traversal()
        return ele

    def level_order(self):
        if self is None:
            return
        queue = [self]
        while len(queue) > 0:
            print(queue[0].data)
            element = queue.pop(0)
            if element.left:
                queue.append(element.left)
            if element.right:
                queue.append(element.right)


def build_tree(elements):
    root = BinaryTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root


if __name__ == '__main__':
    # You can also use strings in list
    list_of_inputs = [15, 12, 14, 7, 20, 27, 88, 23]
    node = build_tree(list_of_inputs)
    print(node.inorder_traversal())
    node.level_order()
