from typing import List, Tuple, Dict
from collections import deque, defaultdict

class DirectedGraph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            print(f"Vertex {vertex} added to the graph.")
            return
        print(f"Vertex {vertex} already exists in the graph.")

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list:
            del self.adjacency_list[vertex]
            print(f"Vertex {vertex} removed from the graph.")

            for other_vertex in self.adjacency_list:
                self.adjacency_list[other_vertex].remove(vertex)
            return

        print(f"Vertex {vertex} does not exist in the graph.")

    def add_edge(self, vertex_start, vertex_end):
        if vertex_start in self.adjacency_list and vertex_end in self.adjacency_list:
            self.adjacency_list[vertex_start].append(vertex_end)
            print(f"Directed edge added from {vertex_start} to {vertex_end}.")
            return

        print(f"Vertices {vertex_start} or {vertex_end} do not exist in the graph.")

    def remove_edge(self, vertex_start, vertex_end):
        if vertex_start in self.adjacency_list and vertex_end in self.adjacency_list:
            self.adjacency_list[vertex_start].remove(vertex_end)
            print(f"Directed edge removed from {vertex_start} to {vertex_end}.")
            return

        print(f"Vertices {vertex_start} or {vertex_end} do not exist in the graph.")

    def vertex_exists(self, vertex):
        exists = vertex in self.adjacency_list
        print(f"Vertex {vertex} exists in the graph: {exists}.")
        return exists

    def edge_exists(self, vertex_start, vertex_end):
        exists = vertex_start in self.adjacency_list and vertex_end in self.adjacency_list[vertex_start]
        print(f"Directed edge from {vertex_start} to {vertex_end} exists: {exists}.")
        return exists

    def get_all_vertices(self) -> List:
        vertices = list(self.adjacency_list.keys())
        print("All vertices in the graph: " + ", ".join(map(str, vertices)))
        return vertices

    def get_all_edges(self) -> List[Tuple]:
        edges = [(vertex, neighbor) for vertex in self.adjacency_list for neighbor in self.adjacency_list[vertex]]
        print("All directed edges in the graph: " + ", ".join(map(str, edges)))
        return edges

    def traverse_bfs(self, start_vertex) -> List:
        visited = []
        queue = deque()

        if start_vertex not in self.adjacency_list:
            print(f"Vertex {start_vertex} does not exist in the graph.")
            return visited

        visited.append(start_vertex)
        queue.append(start_vertex)

        while queue:
            current_vertex = queue.popleft()

            for neighbor in self.adjacency_list[current_vertex]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)

        print("BFS traversal result: " + ", ".join(map(str, visited)))
        return visited

    def calculate_degree(self, vertex) -> int:
        out_degree = len(self.adjacency_list.get(vertex, []))
        print(f"Out-degree of vertex {vertex}: {out_degree}.")
        return out_degree

    def calculate_bfs_levels(self, start_vertex) -> Dict:
        levels = {}
        queue = deque()

        if start_vertex not in self.adjacency_list:
            print(f"Vertex {start_vertex} does not exist in the graph.")
            return levels

        levels[start_vertex] = 0
        queue.append(start_vertex)

        while queue:
            current_vertex = queue.popleft()

            for neighbor in self.adjacency_list[current_vertex]:
                if neighbor not in levels:
                    levels[neighbor] = levels[current_vertex] + 1
                    queue.append(neighbor)

        print("BFS levels: " + ", ".join(f"{key}:{value}" for key, value in levels.items()))
        return levels
    