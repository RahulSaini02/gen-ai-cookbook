# insertion_sort.py

import sys
import os

# Add parent directory to the system path to import shared utilities
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils import log_time


@log_time
def insertion_sort(elements):
    """
    Sorts the input list using the Insertion Sort algorithm.
    This function sorts the list in-place.

    Args:
        elements (list): List of elements to be sorted.
    """
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1

        # Shift elements of the sorted segment forward if they are greater than anchor
        while j >= 0 and elements[j] > anchor:
            elements[j + 1] = elements[j]
            j -= 1

        # Insert anchor in its correct location
        elements[j + 1] = anchor


if __name__ == "__main__":
    # Example and test cases
    tests = [
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],  # Already sorted
        [25, 22, 21, 10],  # Reverse sorted
        [29, 15, 28],  # Small random list
        [],  # Empty list
        [6],  # Single element
    ]

    for test in tests:
        insertion_sort(test)
        print(f"sorted array: {test}")
