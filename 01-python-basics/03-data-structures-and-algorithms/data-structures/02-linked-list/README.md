 # 🔗 Linked List

A **linked list** is a linear data structure where each element (called a node) contains a value and a reference (or pointer) to the next node in the sequence. Unlike arrays, linked lists **do not store elements in contiguous memory locations**. Instead, each node is stored at a different memory location and linked using references.

Linked lists are designed to overcome limitations of arrays, particularly:

- Fixed size (arrays require predefined space)
- Expensive insertions and deletions at arbitrary positions

## ✅ Advantages of Linked Lists over Arrays

- **Dynamic memory allocation** – No need to pre-allocate size.
- **Efficient insertions/deletions** – Especially at the beginning or in the middle of the list.

## Types of Linked Lists

- **Singly Linked List** – Each node has a reference to the next node only.
- **Doubly Linked List** – Each node has references to both the previous and next nodes.

### Singly Linked List Example

```
head → [A | ●] → [B | ●] → [C | ●] → [D | NULL]
        ↑         ↑         ↑         ↑
       Data      Data      Data      Data
```

Each **node** holds data and a pointer to the next node. The last node points to `NULL`, indicating the end of the list.


## Doubly Linked List

In a **doubly linked list**, each node contains:

- A pointer to the previous node
- The data
- A pointer to the next node

This allows traversal in both directions.

### Doubly Linked List Example

```
NULL ← [A | ● | ●] ←→ [B | ● | ●] ←→ [C | ● | ●] ←→ [D | ● | NULL]
        ↑              ↑              ↑              ↑
       Data           Data           Data           Data
```

- Each `[Data | Prev | Next]` box represents a node.
- Arrows `←→` show that each **node** links to both its previous and next neighbor.
- The list begins with `NULL` and ends with `NULL` to indicate no further nodes in that direction.


## Linked List vs Array (Time Complexities)

|                                |    Array             | Linked List | 
|--------------------------------|----------------------|-------------|
| Indexing                       |    O(1)              |   O(n)      |
| Insert/Delete Element at Start |    O(n)              |   O(1)      |
| Insert/Delete Element at End   |    O(1) - amortized  |   O(n)      |
| Insert element in middle       |    O(n)              |   O(n)      |