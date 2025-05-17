import random
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils import log_time

# Increase recursion limit for very deep binary recursions
sys.setrecursionlimit(10**6)


@log_time
def linear_search(nums, key):
    """
    Performs linear search on the list.
    Returns the index of the key if found, else -1.
    """
    for index, element in enumerate(nums):
        if element == key:
            return index
    return -1


@log_time
def binary_search(nums, key):
    """
    Performs iterative binary search on a sorted list.
    Returns the index of the key if found, else -1.
    """
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == key:
            return mid
        elif nums[mid] < key:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def recursive_binary_search(nums, key, left, right):
    """
    Performs recursive binary search on a sorted list.
    Returns the index of the key if found, else -1.
    """
    if right < left:
        return -1

    mid = (left + right) // 2
    if mid >= len(nums) or mid < 0:
        return -1

    if nums[mid] == key:
        return mid
    elif nums[mid] < key:
        return recursive_binary_search(nums, key, mid + 1, right)
    else:
        return recursive_binary_search(nums, key, left, mid - 1)


if __name__ == "__main__":
    N = 100_000_000
    numbers = list(range(N))
    number_to_find = random.randint(0, N - 1)

    print(f"🔍 Searching for number: {number_to_find}")

    index = linear_search(numbers, number_to_find)
    print(f"✅ Found at index {index} using linear search.\n")

    index = binary_search(numbers, number_to_find)
    print(f"✅ Found at index {index} using binary search.\n")

    index = recursive_binary_search(numbers, number_to_find, 0, len(numbers) - 1)
    print(f"✅ Found at index {index} using recursive binary search.\n")
