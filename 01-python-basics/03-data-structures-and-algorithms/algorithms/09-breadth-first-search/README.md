# Breadth First Search (BFS)

**Breadth First Search (BFS)** is a graph traversal method that explores all nodes at the present depth before moving to the next level.

---

## 🔧 How It Works

1. Use a queue to explore neighbors level by level.
2. Start from a node, mark as visited, enqueue its neighbors.
3. Continue until all reachable nodes are visited.

---

## 🧠 Example (Graph):

```
A - B - C
    |   |
    D - E - F
```

Starting at `A`, BFS traversal could be:
```
A B C D E F
```

---

## 📊 Complexity

| Aspect        | Complexity     |
|---------------|----------------|
| Time          | O(V + E)       |
| Space         | O(V)           |

---

## ✅ Advantages

- Finds shortest path in unweighted graphs
- Suitable for level-order traversal

---

## ⚠️ Disadvantages

- Requires more memory due to queue

---