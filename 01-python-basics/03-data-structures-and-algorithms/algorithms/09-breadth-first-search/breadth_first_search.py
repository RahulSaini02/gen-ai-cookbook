# Implementation of Breadth-First Search (BFS) in python

from collections import deque


def bfs(graph, start, visited=None):
    """
    Performs Breadth-First Search (BFS) traversal on a graph.

    Args:
        graph (dict): A dictionary representing an adjacency list of the graph.
        start (str): The starting node for BFS.
        visited (set): A set to track visited nodes.
    """
    if visited is None:
        visited = set()

    queue = deque([start])

    while queue:
        current_node = queue.popleft()

        if current_node not in visited:
            print(current_node, end=" ")
            visited.add(current_node)

            # Add unvisited neighbors to the queue
            queue.extend(graph[current_node] - visited)


if __name__ == "__main__":
    # Sample graph represented as an adjacency list
    graph = {
        "A": {"B"},
        "B": {"A", "C", "D"},
        "C": {"B", "E"},
        "D": {"B", "E"},
        "E": {"C", "D", "F"},
        "F": {"E"},
    }

    print("BFS Traversal starting from node 'A':")
    bfs(graph, "A")
    print()
