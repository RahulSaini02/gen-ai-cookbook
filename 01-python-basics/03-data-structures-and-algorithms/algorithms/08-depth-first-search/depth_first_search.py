# Implementation of Depth-First Search (DFS) in python


def dfs(graph, start, visited=None):
    """
    Performs Depth-First Search (DFS) traversal on a graph.

    Args:
        graph (dict): A dictionary representing an adjacency list of the graph.
        start (str): The starting node for DFS.
        visited (set): A set to track visited nodes.
    """
    if visited is None:
        visited = set()

    if start not in visited:
        print(start, end=" ")
        visited.add(start)

        # Visit all unvisited neighbors
        for neighbor in graph[start] - visited:
            dfs(graph, neighbor, visited)


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

    print("DFS Traversal starting from node 'A':")
    dfs(graph, "A")
    print()
