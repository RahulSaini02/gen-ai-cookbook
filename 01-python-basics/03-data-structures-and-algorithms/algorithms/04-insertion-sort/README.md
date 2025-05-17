# Insertion Sort

**Insertion sort** is a simple sorting algorithm that works by iteratively inserting each element of an unsorted list into its correct position in a sorted portion of the list. It is like sorting playing cards in your hands. You split the cards into two groups: the sorted cards and the unsorted cards. Then, you pick a card from the unsorted group and put it in the right place in the sorted group.

## 🔁 How It Works

1. Start with the second element, assuming the first is already sorted.
2. Compare it with the elements before it.
3. Shift all larger elements one position to the right.
4. Insert the current element into its correct place.
5. Repeat the process for each element in the array.

## 🧠 Algorithm Intuition

- Divide the list into two parts: **sorted** and **unsorted**.
- Repeatedly take the first element from the unsorted part and insert it into the correct position in the sorted part.

## Complexity Analysis of Insertion Sort

### Time Complexity

| Case        | Time Complexity | Reason |
| ----------- | --------------- | ------ |
| **Best**    | O(n)            | If the list is already sorted, where n is the number of elements in the list. |
| **Average** | O(n²)           | If the list is randomly ordered |
| **Worst**   | O(n²)           | If the list is in reverse order|


## Space Complexity

- **Auxiliary Space:** `O(1)`, Insertion sort requires `O(1)` additional space, making it a space-efficient sorting algorithm.

## Advantages and Disadvantages of Insertion Sort

### Advantages

- Simple and easy to implement.
- Stable sorting algorithm.
- Efficient for small lists and nearly sorted lists.
- Space-efficient as it is an in-place algorithm.
- Adoptive. the number of inversions is directly proportional to number of swaps. For example, no swapping happens for a sorted array and it takes O(n) time only.

### Disadvantages

- Inefficient for large lists.
- Not as efficient as other sorting algorithms (e.g., merge sort, quick sort) for most cases.