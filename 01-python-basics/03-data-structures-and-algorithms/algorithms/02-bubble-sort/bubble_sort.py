import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils import log_time


@log_time
def bubble_sort(elements):
    size = len(elements)

    for i in range(0, size - 1):
        swapped = False
        for j in range(0, size - 1 - i):
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
                swapped = True

        if not swapped:
            break


if __name__ == "__main__":
    elements = [5, 9, 2, 1, 67, 34, 88, 34]

    bubble_sort(elements)
    print(elements)
