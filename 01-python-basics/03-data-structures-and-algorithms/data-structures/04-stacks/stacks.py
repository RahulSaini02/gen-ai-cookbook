from collections import deque


class Stack:
    """
    A simple stack implementation using collections.deque for efficient push/pop operations.
    """

    def __init__(self):
        """
        Initializes an empty stack.
        """
        self.container = deque()

    def push(self, val):
        """
        Pushes a value onto the stack.

        Args:
            val: Value to be pushed.
        """
        self.container.append(val)

    def pop(self):
        """
        Removes and returns the top value from the stack.

        Returns:
            The top element if stack is not empty; otherwise raises IndexError.
        """
        if self.empty():
            raise IndexError("Pop from an empty stack")
        return self.container.pop()

    def top(self):
        """
        Returns the top element of the stack without removing it.

        Returns:
            The top element if stack is not empty; otherwise raises IndexError.
        """
        if self.empty():
            raise IndexError("Top of an empty stack")
        return self.container[-1]

    def size(self):
        """
        Returns the number of elements in the stack.
        """
        return len(self.container)

    def empty(self):
        """
        Checks whether the stack is empty.

        Returns:
            True if the stack is empty, False otherwise.
        """
        return len(self.container) == 0

    def __str__(self):
        """
        Returns a string representation of the stack.
        """
        return "Stack (top → bottom): " + " → ".join(map(str, reversed(self.container)))


if __name__ == "__main__":
    st = Stack()

    print("Inserting elements into stack:")
    for val in [5, 10, 15, 20, 25]:
        st.push(val)
        print(f"Pushed: {val}")

    print("\nCurrent Stack:")
    print(st)

    print(f"\nTop of stack: {st.top()}")
    print(f"Stack size: {st.size()}")

    print("\nPopping elements:")
    while not st.empty():
        print(f"Popped: {st.pop()}")

    print(f"\nStack empty: {st.empty()}")
