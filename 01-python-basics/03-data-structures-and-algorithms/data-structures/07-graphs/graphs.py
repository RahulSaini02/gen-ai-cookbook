class Graph:
    """
    A class representing a directed graph using an adjacency list.
    """

    def __init__(self, edges):
        """
        Initializes the graph from a list of edges (tuples).

        Args:
            edges (list): A list of tuples representing edges (from, to)
        """
        self.edges = edges
        self.graph_dict = self._build_graph()

    def _build_graph(self):
        """
        Constructs an adjacency list from the list of edges.

        Returns:
            dict: A dictionary where keys are start nodes and values are lists of end nodes.
        """
        graph = {}
        for start, end in self.edges:
            if start in graph:
                graph[start].append(end)
            else:
                graph[start] = [end]
        return graph

    def get_paths(self, start, end, path=None):
        """
        Finds all possible paths from start to end node.
          - It adds the current start node to the current path.
          - If the current node is equal to the end node, it returns the current path as a completed route.
          - If the current node has no outgoing edges (i.e., it's not in the graph), it returns an empty list.
          - Otherwise, for every child of the current node that hasn’t been visited yet (to avoid cycles), it:
          - Recursively explores paths from that child to the end node
          - Adds all returned paths to the overall result list

        Args:
            start (str): The starting node.
            end (str): The target node.
            path (list): Used internally to track the current path.

        Returns:
            list: A list of all paths from start to end.
        """
        if path is None:
            path = []

        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths

    def get_shortest_path(self, start, end, path=None):
        """
        Finds the shortest path (by number of nodes) from start to end.
          - Just like get_paths, it adds the current node to the path.
          - If the current node is the destination, it returns the path as-is.
          - If there are no outgoing edges, it returns None.
          - For each unvisited child node:
              - It recursively finds the shortest path from that child to end
              - If a path is found and it's shorter than any previously found path, it updates the shortest_path

        Args:
            start (str): The starting node.
            end (str): The target node.
            path (list): Used internally to track the current path.

        Returns:
            list or None: The shortest path as a list of nodes, or None if no path exists.
        """
        if path is None:
            path = []

        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp and (shortest_path is None or len(sp) < len(shortest_path)):
                    shortest_path = sp

        return shortest_path


if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    graph = Graph(routes)

    start = "Paris"
    end = "New York"

    print(f"All paths from {start} to {end}:")
    for path in graph.get_paths(start, end):
        print(" → ".join(path))

    print(f"\nShortest path from {start} to {end}:")
    print(" → ".join(graph.get_shortest_path(start, end)))
