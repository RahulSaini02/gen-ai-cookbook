# Stack

A **stack** is a linear data structure that follows the **Last-In-First-Out (LIFO)** principle — the last element added is the first one to be removed. In other words, insertions and deletions happen from the **same end**, often referred to as the "top" of the stack.

Typical stack operations:
- `push()` – Insert an element
- `pop()` – Remove the top element
- `top()` or `peek()` – View the top element
- `empty()` – Check if the stack is empty
- `size()` – Get the number of elements in the stack

---

## Time Complexity

| Operation       | Time Complexity |
|----------------|-----------------|
| `push()`       | O(1)            |
| `pop()`        | O(1)            |
| `top()` / `peek()` | O(1)        |
| `empty()`      | O(1)            |
| `size()`       | O(1)            |
| Find/Search    | O(n)            |

---

## Stack Implementations in Python

There are multiple ways to implement a stack in Python using built-in data structures or modules:

### ✅ 1. Using `list`

Python’s `list` can act as a stack using:
- `append()` for `push`
- `pop()` for `pop`

However, Python lists store elements in contiguous memory, which can cause **performance issues** (like reallocation delays) as the stack grows.

### ✅ 2. Using `collections.deque` (Recommended)

The `deque` class from Python’s `collections` module is **optimized for fast appends and pops** from both ends. It is generally preferred for implementing stacks because:

- Provides **O(1)** time complexity for `append()` and `pop()`
- Avoids memory reallocation overhead seen in `list`

### ✅ 3. Using `queue.LifoQueue`

This is a thread-safe stack implementation from the `queue` module. It’s suitable for multi-threaded environments, though it comes with slightly more overhead.

---

## 📌 Summary

| Feature         | `list`      | `collections.deque` | `queue.LifoQueue` |
|----------------|-------------|----------------------|-------------------|
| Performance    | Slower as it grows | Fast and efficient | Thread-safe but heavier |
| Ease of use    | Simple      | Simple               | Requires import   |
| Thread Safety  | ❌          | ❌                   | ✅                |
