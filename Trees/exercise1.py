# Question in https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/7_Tree
# /7_tree_exercise.md

class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
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

    def print_tree(self, name=False, designation=False, both=False):
        # Print in hierarchy
        # utilise the level of nodes
        level = self.get_level()
        spaces = '  ' * level * 3
        prefix = spaces + '|__>' if self.parent else ""
        if name:
            print(prefix + self.name)
            if self.children:
                for child in self.children:
                    child.print_tree(name=True)
        elif designation:
            print(prefix + self.designation)
            if self.children:
                for child in self.children:
                    child.print_tree(designation=True)
        elif both:
            print(prefix + self.name + ' (' + self.designation + ')')
            if self.children:
                for child in self.children:
                    child.print_tree(both=True)


def build_tree():
    root = TreeNode("Nilupul", "CEO")
    node_1 = TreeNode("Chinmay", "CTO")
    root.add_child(node_1)
    node_2 = TreeNode("Gels", "HR Head")
    root.add_child(node_2)
    node_3 = TreeNode("Vishwa", "Infrastructure Head")
    node_1.add_child(node_3)
    node_1.add_child(TreeNode("Aamir", "Application Head"))
    node_3.add_child(TreeNode("Dhaval", "Cloud Manager"))
    node_3.add_child(TreeNode("Abhijit", "App Manager"))
    node_2.add_child(TreeNode("Peter", "Recruitment Head"))
    node_2.add_child(TreeNode("Waqas", "Policy Manager"))
    return root


main_node = build_tree()
main_node.print_tree(name=True)
main_node.print_tree(designation=True)
main_node.print_tree(both=True)
