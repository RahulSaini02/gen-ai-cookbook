# Implementation of Selection Sort in python


def selection_sort(arr):
    """
    Sorts the given list in-place using the Selection Sort algorithm.

    Args:
        arr (list): List of elements to sort.
    """
    size = len(arr)

    for i in range(size - 1):
        min_index = i

        # Find the index of the minimum element in the remaining unsorted array
        for j in range(i + 1, size):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first unsorted element
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == "__main__":
    test_cases = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],  # Descending
        [],  # Empty list
        [1, 5, 8, 9],  # Already sorted
        [234, 3, 1, 56, 34, 12, 9, 12, 1300],  # Random values
        [78, 12, 15, 8, 61, 53, 23, 27],  # Another mix
        [5],  # Single element
    ]

    for elements in test_cases:
        selection_sort(elements)
        print(f"sorted array: {elements}")
