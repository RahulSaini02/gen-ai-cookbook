# Trees

The `Tree` data structure is similar to Linked Lists in that each node contains data and can be linked to other nodes. Tree data structure is used to represent hierarchical data.

## Use Cases

The Tree data structure can be useful in many cases:

  - **Hierarchical Data:** File systems, organizational models, etc.
  - **Databases:** Used for quick data retrieval.
  - **Routing Tables:** Used for routing data in network algorithms.
  - **Sorting/Searching:** Used for sorting data and searching for data.
  - **Priority Queues:** Priority queue data structures are commonly implemented using trees, such as binary heaps.

```
             R
          /  |  \
        A    B    C
       / \      / | | \
      D   E    F  G H  I
```

## Tree Terminology

  - The first node in a `tree` is called the `root node`.
  - A link connecting one node to another is called an `edge`.
  - A parent node has links to its child nodes. Another word for a parent node is `internal node`.
  - A node can have zero, one, or many child nodes.
  - A node can only have **one parent node**.
  - Nodes without links to other child nodes are called `leaves`, or `leaf nodes`.
  - The tree height is the **maximum number of edges** from the **root node** to a `leaf node`.
  - The height of a node is the maximum number of edges between the node and a leaf node.
  - The tree size is the number of nodes in the `tree`.

## Types of Trees

Trees are a fundamental data structure in computer science, used to represent hierarchical relationships.

**Binary Trees:** Each node has up to two children, the left child node and the right child node. This structure is the foundation for more complex tree types like Binay Search Trees and AVL Trees.

**Binary Search Trees (BSTs):** A type of Binary Tree where for each node, the left child node has a lower value, and the right child node has a higher value.

**AVL Trees:** A type of Binary Search Tree that self-balances so that for every node, the difference in height between the left and right subtrees is at most one. This balance is maintained through rotations when nodes are inserted or deleted.

### Binary Trees

A **Binary Tree** is a type of tree data structure where each node can have a maximum of two child nodes, a left child node and a right child node.

This restriction, that a node can have a maximum of two child nodes, gives us many benefits:

  - Algorithms like traversing, searching, insertion and deletion become easier to understand, to implement, and run faster.
  - Keeping data sorted in a Binary Search Tree (BST) makes searching very efficient.
  - Balancing trees is easier to do with a limited number of child nodes, using an AVL Binary Tree for example.
  - Binary Trees can be represented as arrays, making the tree more memory efficient.

#### **Binary Tree Terminology**
  - A `parent node`, or `internal node`, in a Binary Tree is a node with one or two child nodes.
  - The` left child node` is the child node to the left.
  - The `right child node` is the child node to the right.
  - The `tree height` is the maximum number of edges from the root node to a leaf node.

#### Types of Binary Trees

There are different variants, or types, of Binary Trees worth discussing to get a better understanding of how Binary Trees can be structured.


  - A `balanced Binary Tree` has at most 1 in difference between its left and right subtree heights, for each node in the tree.

  ```
         11
        /   \
       7     15
      / \   /  \
    3    9 13   19
                \
                18
  ```

  - A `complete Binary Tree` has all levels full of nodes, except the last level, which is can also be full, or filled from left to right. The properties of a complete Binary Tree means it is also balanced.

  ```
              11
            /    \
          7       15
        / \     /  \
        3   9  13  19
      / \   \
      2   4   8
  ```

  - A `full Binary Tree` is a kind of tree where each node has either 0 or 2 child nodes.

  ```
        11
       /  \
     7     15
          /  \
        13    19
       /  \
     12    14
  ```

  - A `perfect Binary Tree` has all leaf nodes on the same level, which means that all levels are full of nodes, and all internal nodes have two child nodes.The properties of a perfect Binary Tree means it is also full, balanced, and complete.

  ```
         11
        /  \
      7     15
     / \   /  \
    3   9 13  19
  ```

