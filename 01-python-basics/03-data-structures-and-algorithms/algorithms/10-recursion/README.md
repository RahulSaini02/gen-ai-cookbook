# 🔁 Recursion

**Recursion** is a programming technique where a function calls itself to solve smaller instances of the same problem.

---

## 🔧 How It Works

1. A problem is broken down into smaller sub-problems.
2. Each sub-problem is solved using the same function.
3. A base case stops the recursion.

---

## 🧠 Examples

### Sum of Numbers
```python
def find_sum(n):
    if n == 1:
        return 1
    return n + find_sum(n - 1)
```

### Fibonacci Sequence
```python
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

---

## 📊 Complexity (Fibonacci Example)

| Approach      | Time        | Space      |
|---------------|-------------|------------|
| Naive         | O(2ⁿ)       | O(n)       |
| With Memoization | O(n)     | O(n)       |

---

## ✅ Advantages

- Elegant and concise
- Useful for divide-and-conquer problems

---

## ⚠️ Disadvantages

- Can be inefficient (stack overflow, redundancy)
- Requires base cases to avoid infinite recursion

---