class BinarySearchTree:
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
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def inorder_traversal(self):
        ele = []
        if self.left:
            ele += self.left.inorder_traversal()
        ele.append(self.data)
        if self.right:
            ele += self.right.inorder_traversal()
        return ele

    def pre_order_traversal(self):
        ele = []
        ele.append(self.data)
        if self.left:
            ele += self.left.pre_order_traversal()
        if self.right:
            ele += self.right.pre_order_traversal()
        return ele

    def post_order_traversal(self):
        ele = []
        if self.left:
            ele += self.left.post_order_traversal()
        if self.right:
            ele += self.right.post_order_traversal()
        ele.append(self.data)
        return ele

    def search(self, val):  # O(log N)
        if self.data == val:
            print("found")
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                print("Not found")
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                print("Not found")
                return False

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return left_sum+self.data+right_sum



def build_tree(elements):
    root = BinarySearchTree(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root


if __name__ == '__main__':
    # You can also use strings in list
    list_of_inputs = [15, 12, 14, 7, 20, 27, 88, 23, 15]
    node = build_tree(list_of_inputs)
    print(node.inorder_traversal())
    print(node.pre_order_traversal())
    print(node.post_order_traversal())
    print(node.search(12))
    print(node.search(0))
    minimum, maximum = node.find_min(), node.find_max()
    print("Minimum is {} and Maximum is {}".format(minimum, maximum))
    print("Sum of nodes in a tree {} ".format(node.calculate_sum()))
