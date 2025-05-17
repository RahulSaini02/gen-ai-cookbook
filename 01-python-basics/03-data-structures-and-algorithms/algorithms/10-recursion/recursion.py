# Implementation of recursions in python


def find_sum(n):
    """
    Recursively calculates the sum of all integers from 1 to n.

    Args:
        n (int): The upper limit of the range.

    Returns:
        int: The sum of all integers from 1 to n.
    """
    if n == 1:
        return 1
    return n + find_sum(n - 1)


def fib(n):
    """
    Recursively calculates the nth Fibonacci number.

    Args:
        n (int): The index in the Fibonacci sequence.

    Returns:
        int: The nth Fibonacci number.
    """
    # Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, ...
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    # Test the recursive sum
    print("Sum from 1 to 5:", find_sum(5))  # Output: 15

    # Test the Fibonacci function
    print("10th Fibonacci number:", fib(10))  # Output: 55
