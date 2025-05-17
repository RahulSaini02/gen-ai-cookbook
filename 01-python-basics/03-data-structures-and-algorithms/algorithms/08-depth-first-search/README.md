# Depth First Search (DFS)

**Depth First Search (DFS)** is a graph traversal technique that explores as far along each branch as possible before backtracking.

---

## 🔧 How It Works

1. Start at the root (or any node).
2. Visit the node and mark it as visited.
3. Recursively visit all unvisited neighbors.

---

## 🧠 Example (Graph):

```
A - B - C
    |   |
    D - E - F
```

Starting at `A`, DFS traversal could be:
```
A B C E D F
```

---

## 📊 Complexity

| Aspect        | Complexity     |
|---------------|----------------|
| Time          | O(V + E)       |
| Space         | O(V)           |

---

## ✅ Advantages

- Simple to implement
- Useful for cycle detection, pathfinding

---

## ⚠️ Disadvantages

- Can get stuck in deep paths without finding the solution (no shortest path guarantee)

---