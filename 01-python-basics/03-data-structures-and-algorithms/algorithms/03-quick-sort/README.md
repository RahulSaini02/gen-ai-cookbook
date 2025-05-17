# 🔄 Quick Sort

**QuickSort** is an efficient, in-place, divide-and-conquer sorting algorithm. It works by selecting a *pivot* element and partitioning the array such that elements smaller than the pivot are on the left, and elements greater than the pivot are on the right. This process is recursively applied to the sub-arrays.

---

## Key Steps in QuickSort

1. **Choose a Pivot:** Select an element from the array. Choices vary: first, last, random, or median.
2. **Partition the Array:** Rearrange elements around the pivot so that:
   - All elements smaller than the pivot come before it.
   - All greater elements come after it.
3. **Recursive Sort:** Apply the same logic to the left and right sub-arrays.
4. **Base Case:** Stop when sub-array has one or zero elements.

---

## 🎯 Pivot Selection Strategies

- **First/Last Element:** Simple but leads to worst-case performance on sorted arrays.
- **Random Element:** Avoids worst-case for sorted input; improves average performance.
- **Median of Three or True Median:** Gives optimal partitioning but is more complex and slower in practice.

---

## ⚙️ Partitioning Schemes

The **partition()** function is the core of `QuickSort`. It determines where the pivot ends up and how the rest of the array is rearranged. Below are the three major schemes:

| Scheme       | Description                                                                 | Time | Space | In-place | Notes                           |
|--------------|-----------------------------------------------------------------------------|------|-------|----------|---------------------------------|
| **Naive**    | Create a temporary array for smaller & larger elements. Copy back to original. | O(n) | O(n)  | ❌        | Easy but memory inefficient     |
| **Lomuto**   | Use a single pointer to track elements ≤ pivot. Swap as needed.             | O(n) | O(1)  | ✅        | Simple, but performs more swaps |
| **Hoare**    | Two pointers from both ends move toward each other, swapping misplaced elements. | O(n) | O(1)  | ✅        | Fewer swaps, faster in practice |

> **Note:** Hoare's scheme doesn’t place the pivot in its final position, so recursive calls differ from Lomuto's.

---

### ✅ Summary of Hoare’s Partition

- Picks the **first** element as pivot.
- Initializes two pointers:
  - `left` starts from `start - 1`
  - `right` starts from `end + 1`
- Moves `left` rightward until it finds an element ≥ pivot.
- Moves `right` leftward until it finds an element ≤ pivot.
- If `left` < `right`, swap them.
- When pointers cross, return `right` (partition index).
