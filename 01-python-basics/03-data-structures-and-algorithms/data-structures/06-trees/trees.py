class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent

        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        prefix = " " * self.get_level() * 2
        print(f"{prefix} + {self.data}")
        if self.children:
            for child in self.children:
                child.print_tree()


def build_tree():
    root = TreeNode("R")

    A = TreeNode("A")
    A.add_child(TreeNode("D"))
    A.add_child(TreeNode("E"))

    B = TreeNode("B")

    C = TreeNode("C")
    C.add_child(TreeNode("F"))
    C.add_child(TreeNode("G"))
    C.add_child(TreeNode("H"))
    C.add_child(TreeNode("I"))

    root.add_child(A)
    root.add_child(B)
    root.add_child(C)

    return root


if __name__ == "__main__":
    root = build_tree()
    root.print_tree()
