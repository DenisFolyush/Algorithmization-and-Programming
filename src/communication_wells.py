import csv

from collections import defaultdict


class Graph:
    """Class to represent a weighted undirected graph."""

    def __init__(self):
        """Initialize an empty graph."""
        self.graph = defaultdict(dict)

    def add_edge(self, source_vertex, destination_vertex, weight):
        """Add an edge between vertices `source_vertex` and `destination_vertex` with the given `weight`.

        Args:
            source_vertex (hashable): The first vertex. #hashable?
            destination_vertex (hashable): The second vertex. #hashable?
            weight (numeric): The weight of the edge. #numeric?
        """
        self.graph[source_vertex][destination_vertex] = weight
        self.graph[destination_vertex][source_vertex] = weight

    def prim_mst(self):
        """Compute the minimum spanning tree of the graph using Prim's algorithm.

        Returns:
            list: A list of tuples representing the edges in the minimum spanning tree.
                  Each tuple contains three elements: (parent_vertex, current_vertex, weight).
        """
        min_span_tree = []
        visited = set()

        start_vertex = next(iter(self.graph))
        vertex_queue = [(0, start_vertex, None)]

        while vertex_queue:
            weight, current_vertex, parent = vertex_queue.pop(0)

            if current_vertex not in visited:
                min_span_tree.append((parent, current_vertex, weight))
                visited.add(current_vertex)

                for neighbor, edge_weight in self.graph[current_vertex].items():
                    if neighbor not in visited:
                        vertex_queue.append((edge_weight, neighbor, current_vertex))

                vertex_queue.sort()

        return min_span_tree


def read_graph_from_csv(file_name):
    """Read the graph data from a CSV file.

    Args:
        file_name (str): The name of the CSV file containing the graph data.

    Returns:
        Graph: The graph object.
    """
    g = Graph()
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                well1, well2, distance = row
                g.add_edge(well1.strip(), well2.strip(), int(distance))
            except ValueError:
                print(f"Skipping invalid row: {row}")

    return g


def compute_min_cable_length(input_file_name, output_file_name):
    """Compute the minimum cable length of the graph and write it to the output file."""
    graph = read_graph_from_csv(input_file_name)

    if not graph.graph:
        min_cable_length = -1
    else:
        mst = graph.prim_mst()
        min_cable_length = sum(weight for _, _, weight in mst)

    with open(output_file_name, "w") as file:
        file.write(str(min_cable_length))