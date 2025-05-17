# Selection Sort

**Selection Sort** is a simple in-place comparison sorting algorithm. It repeatedly finds the minimum element and places it at the beginning.

---

## 🔧 How It Works

1. Start from the beginning of the list.
2. Find the minimum value in the unsorted part.
3. Swap it with the first unsorted element.
4. Move the boundary between sorted and unsorted rightward.

---

## 🧠 Example

Original:
```
[78, 12, 15, 8]
```

Sorted:
```
[8, 12, 15, 78]
```

---

## 📊 Complexity

| Case         | Time   | Space |
|--------------|--------|-------|
| Best         | O(n²)  | O(1)  |
| Average      | O(n²)  | O(1)  |
| Worst        | O(n²)  | O(1)  |

---

## ✅ Advantages

- Easy to understand and implement
- Performs well on small lists

---

## ⚠️ Disadvantages

- Inefficient on large lists
- Not stable

---