class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        if self.data == data:
            return False  # Eliminating duplicate nodes
        elif data < self.data:
            if self.left is None:
                self.left = Tree(data)
                return True
            else:
                return self.left.insert(data)
        else:
            if self.right is None:
                self.right = Tree(data)
                return True
            else:
                return self.right.insert(data)

    def find(self, data):

        if self.data == data:
            return data
        elif data < self.data:
            if self.left is None:
                return False
            else:
                self.left.find(data)
        else:
            if self.right is None:
                return False
            else:
                return self.right.find(data)

    def size_of_tree(self):
        if self.left is not None and self.right is not None:
            return 1 + self.left.size_of_tree() + self.right.size_of_tree()
        elif self.left:
            return 1 + self.left.size_of_tree()
        elif self.right:
            return 1 + self.right.size_of_tree()
        else:
            return 1

    def preorder_traverse(self):
        if self is not None:
            print(self.data, end=' ')
            if self.left is not None:
                self.left.preorder_traverse()
            if self.right is not None:
                self.right.preorder_traverse()

    def inorder_traverse(self):
        if self is not None:
            if self.left is not None:
                self.left.inorder_traverse()
            print(self.data, end=' ')
            if self.right is not None:
                self.right.inorder_traverse()


if __name__ == "__main__":
    tree = Tree(10)
    tree.insert(11)
    for i in range(3, 12):
        tree.insert(i)
    tree.inorder_traverse()  # Prints in sorted order
    print()
    tree.preorder_traverse()
    found = tree.find(11)
    print()
    print("element searched ", found)
