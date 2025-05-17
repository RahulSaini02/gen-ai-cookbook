# Implementation of Merge Sort in python


def merge_sort(arr):
    """
    Sorts the given list in-place using the Merge Sort algorithm.

    Args:
        arr (list): List of elements to sort.
    """
    if len(arr) <= 1:
        return

    # Find the midpoint and divide the array
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort both halves
    merge_sort(left)
    merge_sort(right)

    # Merge the sorted halves back into the original array
    merge_two_sorted_lists(left, right, arr)


def merge_two_sorted_lists(a, b, arr):
    """
    Merges two sorted lists `a` and `b` into `arr` in sorted order.

    Args:
        a (list): First sorted sublist.
        b (list): Second sorted sublist.
        arr (list): Target list to store the merged result.
    """
    i = j = k = 0
    len_a = len(a)
    len_b = len(b)

    # Compare elements from both sublists and insert the smaller one
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1

    # Copy any remaining elements from `a`
    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1

    # Copy any remaining elements from `b`
    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1


if __name__ == "__main__":
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],  # Random order
        [],  # Empty list
        [3],  # Single element
        [9, 8, 7, 2],  # Reverse order
        [1, 2, 3, 4, 5],  # Already sorted
    ]

    for arr in test_cases:
        merge_sort(arr)
        print(f"sorted array: {arr}")
