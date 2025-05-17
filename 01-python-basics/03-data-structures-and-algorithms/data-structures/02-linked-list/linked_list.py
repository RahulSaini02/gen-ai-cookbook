class Node:
    """
    A node in a singly linked list.

    Attributes:
        data: The value stored in the node.
        next: A reference to the next node in the list.
    """

    def __init__(self, data, next):
        """
        Initializes a new node with given data and reference to the next node.

        Args:
            data: Value to store in the node.
            next: Reference to the next node (or None).
        """
        self.data = data
        self.next = next


class LinkedList:
    """
    Singly Linked List implementation with basic operations like insertion, deletion, and traversal.
    """

    def __init__(self):
        """
        Initialize an empty linked list with head set to None.
        """
        self.head = None

    def __str__(self):
        """
        Returns a string representation of the linked list.
        """
        if self.head is None:
            return "Linked list is empty."

        current_node = self.head
        llstr = ""

        while current_node.next:
            llstr += str(current_node.data) + " --> "
            current_node = current_node.next

        llstr += str(current_node.data)
        return llstr

    def print_ll(self):
        """
        Prints all node values in the linked list.
        """
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def get_length(self):
        """
        Returns the number of nodes in the linked list.
        """
        count = 0
        current_node = self.head

        while current_node:
            count += 1
            current_node = current_node.next

        return count

    def insert_at_begin(self, data):
        """
        Inserts a new node with the given data at the beginning of the list.
        """
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        """
        Appends a new node with the given data at the end of the list.
        """
        if self.head is None:
            self.head = Node(data, None)
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = Node(data, None)

    def insert_at_index(self, data, index: int):
        """
        Inserts a node with the given data at the specified index.
        Raises an exception for invalid indices.
        """
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_begin(data)
            return

        count = 0
        current_node = self.head

        while current_node:
            if count == index - 1:
                node = Node(data, current_node.next)
                current_node.next = node
                return
            current_node = current_node.next
            count += 1

    def insert_values(self, data_list: list):
        """
        Replaces the current list with nodes from the provided list.
        """
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def remove_at_index(self, index: int):
        """
        Removes the node at the specified index.
        Raises an exception for invalid indices.
        """
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        current_node = self.head

        while current_node:
            if count == index - 1:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
            count += 1


if __name__ == "__main__":
    ll = LinkedList()

    print("✅ Inserting values at the end:")
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    print(ll)

    print("\n✅ Inserting at the beginning:")
    ll.insert_at_begin(5)
    print(ll)

    print("\n✅ Inserting at index 2:")
    ll.insert_at_index(15, 2)
    print(ll)

    print("\n✅ Removing node at index 3:")
    ll.remove_at_index(3)
    print(ll)

    print("\n✅ Inserting multiple values:")
    ll.insert_values([100, 200, 300, 400])
    print(ll)

    print("\n✅ Printing values one by one:")
    ll.print_ll()

    print(f"\nLength of linked list: {ll.get_length()}")
