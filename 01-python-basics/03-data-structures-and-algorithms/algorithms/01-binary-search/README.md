# 🔍 Searching Algorithms

Searching is a fundamental operation in computer science used to locate the position of a target element within a data structure.

Two primary searching techniques:

- ✅ Linear Search
- ✅ Binary Search

---

## 🔹 Linear Search

**Linear Search** is the simplest searching technique. It checks every element in a list, one by one, until the desired value is found or the list ends.

### 📌 Characteristics:
- Does **not require sorting**
- Works on any iterable
- Time complexity: **O(n)**

### 🧠 How it works:
- Start at the first element.
- Compare each element with the target value.
- Return the index if a match is found.
- If the end of the list is reached without a match, return -1.

### ❗ Drawbacks:
- Inefficient for large datasets
- Can require scanning all elements in the worst case

---

## 🔹 Binary Search

**Binary Search** is a more efficient technique used on **sorted arrays/lists**. It repeatedly divides the search space in half to locate the target value.

### 📌 Requirements:
- The data must be **sorted** (in ascending or descending order).
- The data structure must allow **random access** (like arrays or lists).

### ⏱ Time Complexity:
- **O(log n)** — much faster than linear search for large datasets

---

## 🧮 Binary Search Algorithm

1. Set the search space: `left = 0`, `right = len(array) - 1`
2. While `left <= right`:
    - Calculate `mid = (left + right) // 2`
    - If `array[mid] == target`, return `mid`
    - If `array[mid] < target`, search the **right half** (`left = mid + 1`)
    - If `array[mid] > target`, search the **left half** (`right = mid - 1`)
3. If the search space is exhausted, return `-1` (not found)

---

## ⚖️ Comparison

| Feature         | Linear Search | Binary Search |
|----------------|---------------|----------------|
| Works on sorted data? | ❌ No        | ✅ Yes          |
| Time Complexity | O(n)         | O(log n)       |
| Simplicity      | ✅ Simple    | ⚠️ Requires more logic |
| Use Case        | Small or unsorted data | Large, sorted data |

---