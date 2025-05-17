# Queue

Like a `stack`, the `queue` is a linear data structure that stores items in a **First In First Out (FIFO)** manner. With a queue, the least recently added item is removed first.

## Operations associated with queue are: 

| Operation   | Description                                                                           | Time Complexity |
|-------------|---------------------------------------------------------------------------------------|-----------------|
| `enqueue`   | Adds an item to the rear of the queue.                                                | O(1)            |
| `dequeue`   | Removes an item from the front of the queue.                                          | O(1)            |
| `front`     | Returns the front (oldest) item in the queue without removing it.                     | O(1)            |
| `rear`      | Returns the rear (newest) item in the queue without removing it.                      | O(1)            |
| `empty()`   | Returns `True` if the queue is empty, `False` otherwise.                              | O(1)            |
| `size()`    | Returns the number of items in the queue.                                             | O(1)            |

---

## Queue Implementations in Python

There are multiple ways to implement a queue in Python using built-in data structures or modules:

### ✅ 1. Using `list`

Python’s `list` can act as a queue using:
- `append()` for `enqueue`
- `pop()` for `dequeue`

However, Python lists store elements in contiguous memory, which can cause **performance issues** (like reallocation delays) as the queue grows.

### ✅ 2. Using `collections.deque` (Recommended)

The `deque` class from Python’s `collections` module is **optimized for fast appends and pops** from both ends. It is generally preferred for implementing stacks because:

- Provides **O(1)** time complexity for `appendleft()` and `pop()`
- Avoids memory reallocation overhead seen in `list`

### ✅ 3. Using `queue.Queue`

`Queue` is built-in module of Python which is used to implement a queue. queue.Queue(maxsize) initializes a variable to a maximum size of maxsize. A maxsize of zero ‘0’ means a infinite queue. This Queue follows FIFO rule. 
There are various functions available in this module: 

- `maxsize` – Number of items allowed in the queue.
- `empty()` – Return True if the queue is empty, False otherwise.
- `full()` – Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default), then full() never returns True.
- `get()` – Remove and return an item from the queue. If queue is empty, wait until an item is available.
- `get_nowait()` – Return an item if one is immediately available, else raise QueueEmpty.
- `put(item)` – Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
- `put_nowait(item)` – Put an item into the queue without blocking. If no free slot is immediately available, raise QueueFull.
- `qsize()` – Return the number of items in the queue.

---

## 📌 Summary

| Feature     | `list`         | `collections.deque` | `queue.Queue`        |
| ----------- | -------------- | ------------------- | -------------------- |
| Performance | ❌ O(n) pops   | ✅ O(1)             | ✅ O(1)              |
| Thread-Safe | ❌             | ❌                  | ✅                   |
| Use Case    | Learning only  | General-purpose     | Multi-threaded apps  |
