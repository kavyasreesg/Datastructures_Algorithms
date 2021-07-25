import sys

# program to check if a binary tree is bst or not
"""
Approach:
    -   Assign minimum and maximum values to maximum and minimum int values
    -   Base Condition : If node's data < minimum and node's data >
        maximum, return False. Also if node is none, return True
    -   Else, return func(node->left, minimum, node->data -1)
              return func(node->right, node->data +1, maximum)
        This way we are also making sure by not passing node->data to avoid duplicates.
"""
INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize


# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Returns true if the given tree is a binary search tree
# (efficient version)
def isBST(node):
    return isBSTUtil(node, INT_MIN, INT_MAX)


# return true if the given tree is a BST and its values
# >= min and <= max
def isBSTUtil(node, mini, maxi):
    # An empty tree is BST
    if node is None:
        return True

    # False if this node violates min/max constraint
    if node.data < mini or node.data > maxi:
        return False

    # Otherwise check the subtrees recursively
    # tightening the min or max constraint
    return (isBSTUtil(node.left, mini, node.data - 1) and
            isBSTUtil(node.right, node.data + 1, maxi))


# Driver program to test above function
root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

if isBST(root):
    print("Is BST")
else:
    print("Not a BST")
