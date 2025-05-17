from collections import deque


class Queue:
    """
    A simple queue implementation using collections.deque for efficient enqueue/dequeue operations.
    Follows FIFO (First-In-First-Out) behavior.
    """

    def __init__(self):
        """
        Initializes an empty queue.
        """
        self.buffer = deque()

    def enqueue(self, val):
        """
        Adds a value to the end of the queue.

        Args:
            val: Value to be added.
        """
        self.buffer.appendleft(val)

    def dequeue(self):
        """
        Removes and returns the front value from the queue.

        Returns:
            The front element if the queue is not empty.
        Raises:
            IndexError: If the queue is empty.
        """
        if self.empty():
            raise IndexError("Dequeue from an empty queue")
        return self.buffer.pop()

    def size(self):
        """
        Returns the number of elements in the queue.
        """
        return len(self.buffer)

    def empty(self):
        """
        Checks whether the queue is empty.

        Returns:
            True if the queue is empty, False otherwise.
        """
        return len(self.buffer) == 0

    def front(self):
        """
        Returns the front (oldest) element in the queue without removing it.

        Returns:
            The front element in the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.empty():
            raise IndexError("Front from an empty queue")
        return self.buffer[-1]

    def rear(self):
        """
        Returns the rear (most recently added) element in the queue without removing it.

        Returns:
            The rear element in the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.empty():
            raise IndexError("Rear from an empty queue")
        return self.buffer[0]

    def __str__(self):
        """
        Returns a string representation of the queue.
        """
        return "Queue (front → rear): " + " → ".join(map(str, reversed(self.buffer)))


if __name__ == "__main__":
    q = Queue()

    print("Enqueue elements into queue:")
    for val in [5, 10, 15, 20, 25]:
        q.enqueue(val)
        print(f"Enqueued: {val}")

    print("\nCurrent Queue:")
    print(q)

    print("\nFront of the Queue:")
    print(q.front())

    print("\nRear of the Queue:")
    print(q.rear())

    print(f"\nQueue size: {q.size()}")

    print("\nDequeueing elements:")
    while not q.empty():
        print(f"Dequeued: {q.dequeue()}")

    print(f"\nQueue empty: {q.empty()}")
