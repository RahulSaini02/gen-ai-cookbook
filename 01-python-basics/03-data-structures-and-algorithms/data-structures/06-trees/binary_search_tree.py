class BinarySearchTreeNode:
    """
    A node in a binary search tree (BST), supporting insert, delete, search, min/max, and in-order traversal.
    """

    def __init__(self, data):
        """
        Initializes a node with data and optional left/right children.
        """
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        """
        Inserts a new node into the BST following BST rules.
        Duplicate values are ignored.
        """
        if data == self.data:
            return  # No duplicates allowed

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        """
        Returns the elements of the BST in sorted (in-order) order.
        """
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, val):
        """
        Searches for a value in the BST.

        Returns:
            True if found, False otherwise.
        """
        if self.data == val:
            return True

        if val < self.data:
            return self.left.search(val) if self.left else False

        return self.right.search(val) if self.right else False

    def find_max(self):
        """
        Finds the maximum value in the BST.
        """
        return self.data if self.right is None else self.right.find_max()

    def find_min(self):
        """
        Finds the minimum value in the BST.
        """
        return self.data if self.left is None else self.left.find_min()

    def delete(self, val):
        """
        Deletes a node from the BST and returns the modified tree.
        """
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            # Node to delete found
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            # Node with two children: replace with in-order successor
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self


def build_bst(elements):
    """
    Builds a BST from a list of elements and returns the root.
    """
    if not elements:
        return None

    root = BinarySearchTreeNode(elements[0])
    for val in elements[1:]:
        root.add_child(val)
    return root


if __name__ == "__main__":
    # Sample trees
    tree1 = build_bst([17, 4, 1, 20, 9, 23, 18, 34])
    tree2 = build_bst([11, 7, 15, 3, 9, 13, 19])

    print("In-order Traversal (Tree 1):", tree1.in_order_traversal())
    print("In-order Traversal (Tree 2):", tree2.in_order_traversal())

    # Deletion
    tree1.delete(20)
    tree2.delete(13)
    print("\nAfter Deletion:")
    print("Tree 1 after deleting 20:", tree1.in_order_traversal())
    print("Tree 2 after deleting 13:", tree2.in_order_traversal())

    # Search examples
    print("\nSearch:")
    print("Is 9 in Tree 1?", tree1.search(9))
    print("Is 42 in Tree 2?", tree2.search(42))

    # Min/Max
    print("\nMax in Tree 1:", tree1.find_max())
    print("Min in Tree 2:", tree2.find_min())
