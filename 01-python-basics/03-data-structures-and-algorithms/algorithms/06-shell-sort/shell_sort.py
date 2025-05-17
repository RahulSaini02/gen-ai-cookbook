# Implementation of Shell Sort in python


def shell_sort(arr):
    """
    Sorts the given list in-place using Shell Sort algorithm.

    Args:
        arr (list): List of elements to sort.
    """
    size = len(arr)
    gap = size // 2

    # Reduce gap until it becomes 0
    while gap > 0:
        for i in range(gap, size):
            anchor = arr[i]
            j = i

            # Perform gapped insertion sort
            while j >= gap and arr[j - gap] > anchor:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = anchor

        gap //= 2


if __name__ == "__main__":
    test_cases = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],  # Descending order
        [],  # Empty list
        [1, 5, 8, 9],  # Already sorted
        [234, 3, 1, 56, 34, 12, 9, 12, 1300],  # Random elements
        [5],  # Single element
    ]

    for arr in test_cases:
        shell_sort(arr)
        print(f"sorted array: {arr}")
