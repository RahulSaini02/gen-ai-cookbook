# Shell Sort

**Shell Sort** is an in-place comparison sort that generalizes insertion sort to allow exchanges of far-apart elements. It starts by sorting elements far apart from each other and progressively reducing the gap.

---

## 🔧 How It Works

1. Choose an initial large gap and reduce it over time.
2. For each gap, perform insertion sort on sublists of elements spaced by the gap.

---

## 🧠 Example

Initial array:
```
[89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1]
```

Sorted:
```
[1, 2, 6, 7, 9, 12, 17, 21, 23, 53, 61, 78, 89]
```

---

## 📊 Complexity

| Case         | Time         | Space   |
|--------------|--------------|---------|
| Best         | O(n log n)   | O(1)    |
| Average      | O(n log² n)  | O(1)    |
| Worst        | O(n²)        | O(1)    |

---

## ✅ Advantages

- In-place sorting
- Efficient for medium-size lists

---

## ⚠️ Disadvantages

- Unstable sort
- Performance depends on gap sequence

---