# #️⃣ HashMap

A **HashMap** is an indexed data structure that stores data in key-value pairs. It uses a **hash function** to compute an index into an array of buckets (or slots), where the corresponding value is stored. The key must be **unique** and **immutable**.

---

## 🔢 Hash Function

A **hash function** is a mathematical function that converts input data of variable length into a fixed-size output, known as a **hash value**.

Hashing is essential for achieving:
- Fast lookup
- Quick insertion
- Efficient deletion

### Time Complexity (Average Case):
- **Lookup by Key**: `O(1)`
- **Insertion/Deletion**: `O(1)`

---

## Collisions

A **collision** occurs when two different keys produce the same hash index.

To handle collisions, we use strategies like:

### 🔗 Chaining

- Each bucket contains a **linked list** of key-value pairs.
- If multiple keys hash to the same index, they're appended to the list.
- **Drawback**: In worst case, time complexity becomes `O(n)`.

### Linear Probing

- If a bucket is already occupied, look for the **next available slot** linearly.
- All entries remain in the same array, reducing memory usage.
- **Care** must be taken to avoid clustering and infinite loops.

---

## ✅ Summary

| Feature               | HashMap      |
|------------------------|--------------|
| Access by Key          | `O(1)`       |
| Insert/Delete by Key   | `O(1)`       |
| Collision Resolution   | Chaining / Probing |
| Key Requirement        | Unique & Immutable |