# 🔗 Graphs

A **Graph** is a non-linear data structure consisting of **vertices (nodes)** and **edges (connections)**. Graphs are widely used in areas such as:

- 🔍 Social network analysis  
- 🎯 Recommendation systems  
- 🌐 Computer networks  
- 🧠 AI/ML graph embeddings  
- ⚽ Sports analytics (e.g., modeling team dynamics, player interactions)

Formally, a graph is denoted as **G(V, E)** where:
- **V** is the set of vertices (nodes)
- **E** is the set of edges (connections between nodes)

---

## 🧱 Components of a Graph

- **Vertices (Nodes):** The fundamental units of the graph. Each vertex may represent an object (e.g., city, user, player) and can be **labeled or unlabeled**.
  
- **Edges (Links):** Connections between vertices. In **directed graphs**, edges are ordered pairs (A → B). In **undirected graphs**, edges are unordered pairs (A — B). Edges may be **weighted** or **unweighted**.

---

## 🧭 Types of Graphs in Data Structures & Algorithms

Below are commonly encountered graph types:

### 1. **Null Graph**
- A graph with **no edges**.
  
### 2. **Trivial Graph**
- A graph with only **one vertex** and **no edges**.
  
### 3. **Undirected Graph**
- Edges **do not have direction**. Example: A—B means A is connected to B and vice versa.
  
### 4. **Directed Graph (Digraph)**
- Edges have a **specific direction** (A → B).

### 5. **Connected Graph**
- **Every node** is reachable from **any other node** in the graph.

### 6. **Disconnected Graph**
- **At least one node** is not reachable from another node.

### 7. **Regular Graph**
- Every vertex has the **same degree** (i.e., same number of edges). A graph where every node has degree **K** is called a **K-regular graph**.

### 8. **Complete Graph**
- Every node is connected to **every other node** by a unique edge.

### 9. **Cycle Graph**
- A graph where all vertices are connected in a **closed loop**. Every node has a degree of 2.

### 10. **Cyclic Graph**
- A graph that contains **at least one cycle**.

### 11. **Directed Acyclic Graph (DAG)**
- A directed graph that has **no cycles**. Commonly used in scheduling, data pipelines, and dependency resolution.

### 12. **Bipartite Graph**
- Vertices can be divided into **two sets** such that **no edge exists** between nodes in the **same set**.

### 13. **Weighted Graph**
- Each edge is assigned a **weight (cost/value)**. Useful in applications like shortest path (e.g., Dijkstra’s algorithm).  
  - **Directed Weighted Graph** – edges are directional and weighted  
  - **Undirected Weighted Graph** – edges are bidirectional and weighted

---
