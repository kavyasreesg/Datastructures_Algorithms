class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        # Count number of ancestors
        p = self.parent
        level = 0
        while p:
            p = p.parent
            level += 1
        return level

    def print_tree(self, level, temp=0):
        # Print in hierarchy
        # utilise the level of nodes
        temp += 1
        if level >= 0:
            spaces = temp * '  ' if self.parent else ''
            print(spaces + self.data)
            level -= 1
            if self.children:
                for child in self.children:
                    child.print_tree(level, temp)


def build_tree():
    root = TreeNode("Global")
    child_1 = TreeNode("India")
    child_2 = TreeNode("USA")
    child_1_1 = TreeNode("Gujarat")
    child_1_2 = TreeNode("Karnataka")
    child_2_1 = TreeNode("New Jersey")
    child_2_2 = TreeNode("California")
    root.add_child(child_1)
    root.add_child(child_2)
    child_1.add_child(child_1_1)
    child_1.add_child(child_1_2)
    child_2.add_child(child_2_1)
    child_2.add_child(child_2_2)
    child_1_1.add_child(TreeNode("Ahmedabad"))
    child_1_1.add_child(TreeNode("Baroda"))
    child_1_2.add_child(TreeNode("Bengaluru"))
    child_1_2.add_child(TreeNode("Mysore"))
    child_2_1.add_child(TreeNode("Princeton"))
    child_2_1.add_child(TreeNode("Trenton"))
    child_2_2.add_child(TreeNode("San Fransisco"))
    child_2_2.add_child(TreeNode("Mountain View"))
    child_2_2.add_child(TreeNode("Palo Alto"))
    return root


main_node = build_tree()
main_node.print_tree(1)
main_node.print_tree(2)
main_node.print_tree(3)
