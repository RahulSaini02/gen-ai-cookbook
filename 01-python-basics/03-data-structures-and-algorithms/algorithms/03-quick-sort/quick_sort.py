# implementation of quick sort in python using hoare partition scheme


def swap(a, b, arr):
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]


def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi)
        quick_sort(elements, pi + 1, end)


def partition(elements, start, end):
    pivot = elements[start]
    left = start - 1
    right = end + 1

    while True:
        left += 1
        while elements[left] < pivot:
            left += 1

        right -= 1
        while elements[right] > pivot:
            right -= 1

        if left >= right:
            return right

        swap(left, right, elements)


if __name__ == "__main__":
    tests = [
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6],
    ]

    for elements in tests:
        quick_sort(elements, 0, len(elements) - 1)
        print(f"sorted array: {elements}")
