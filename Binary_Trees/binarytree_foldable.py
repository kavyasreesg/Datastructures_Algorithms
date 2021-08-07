"""
If left subtree is mirror of right
Time complexity is O(N)
"""
class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_foldable(root_node):
    if root_node is None:
        return True
    return is_foldable_util(root_node.left, root_node.right)


def is_foldable_util(node1, node2):
    if node1 is None and node2 is None:
        return True

    if node1 is None or node2 is None:
        return False

    return is_foldable_util(node1.left, node2.right) and is_foldable_util(node1.right, node2.left)


root = BinarySearchTree(10)
root.left = BinarySearchTree(7)
root.left.right = BinarySearchTree(9)
root.right = BinarySearchTree(15)
root.right.left = BinarySearchTree(11)
print(is_foldable(root))
