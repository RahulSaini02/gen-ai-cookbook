# Merge Sort

**Merge Sort** is a divide-and-conquer algorithm that breaks down an input list into smaller sublists, sorts them, and then merges them back together to produce the final sorted list.

---

## 🚀 How It Works

1. **Divide** the list into two halves.
2. **Recursively sort** each half.
3. **Merge** the two sorted halves into a sorted whole.

The merge step is key to maintaining the order during recombination.

---

## 🧠 Example

Original list:
```
[10, 3, 15, 7, 8, 23, 98, 29]
```

After sorting:
```
[3, 7, 8, 10, 15, 23, 29, 98]
```

---

## 📊 Complexity

| Case         | Time     | Space   |
|--------------|----------|---------|
| Best         | O(n log n) | O(n)    |
| Average      | O(n log n) | O(n)    |
| Worst        | O(n log n) | O(n)    |

---

## ✅ Advantages

- Stable sort
- Performs well on large data sets

---

## ⚠️ Disadvantages

- Requires additional space (O(n))

---

## 🔗 Use Case

- Sorting linked lists
- External sorting (like sorting files on disk)

---
