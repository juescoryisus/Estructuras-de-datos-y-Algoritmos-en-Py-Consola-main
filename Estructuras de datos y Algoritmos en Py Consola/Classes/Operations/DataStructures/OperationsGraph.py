from Classes.DataStructures.Graphs.Graph import Graph
from Classes.DataStructures.Graphs.DirectedGraph import DirectedGraph


class OperationsGraph:
    @staticmethod
    def all_operation_graph(graph):
        graph_message = "Graph" if isinstance(graph, Graph) else "Directed graph"

        while True:
            print(f"{graph_message} Menu: \n"
                  + "1. Add Vertex\n"
                  + "2. Remove Vertex\n"
                  + "3. Add Edge\n"
                  + "4. Remove Edge\n"
                  + "5. Check Vertex Existence\n"
                  + "6. Check Edge Existence\n"
                  + "7. Get All Vertices\n"
                  + "8. Get All Edges\n"
                  + "9. Traverse BFS\n"
                  + "10. Calculate Vertex Degree\n"
                  + "11. Calculate BFS Levels\n"
                  + "0. Exit\n")

            try:
                choice = int(input())
            except ValueError:
                OperationsGraph.deffault()
                continue

            if choice == 1:
                vertex_value = input("Enter vertex value: ")
                graph.add_vertex(vertex_value)
                print("Vertex added successfully.")

            elif choice == 2:
                vertex_value = input("Enter vertex value to remove: ")
                graph.remove_vertex(vertex_value)

            elif choice == 3:
                vertex_start = input("Enter starting vertex: ")
                vertex_end = input("Enter ending vertex: ")
                graph.add_edge(vertex_start, vertex_end)
                print("Edge added successfully.")

            elif choice == 4:
                vertex_start = input("Enter starting vertex: ")
                vertex_end = input("Enter ending vertex: ")
                graph.remove_edge(vertex_start, vertex_end)

            elif choice == 5:
                vertex_to_check = input("Enter vertex to check existence: ")
                graph.vertex_exists(vertex_to_check)

            elif choice == 6:
                vertex_start = input("Enter starting vertex: ")
                vertex_end = input("Enter ending vertex: ")
                graph.edge_exists(vertex_start, vertex_end)

            elif choice == 7:
                graph.get_all_vertices()

            elif choice == 8:
                graph.get_all_edges()

            elif choice == 9:
                start_vertex_bfs = input("Enter starting vertex for BFS traversal: ")
                graph.traverse_bfs(start_vertex_bfs)

            elif choice == 10:
                vertex_to_calculate_degree = input("Enter vertex to calculate degree: ")
                graph.calculate_degree(vertex_to_calculate_degree)

            elif choice == 11:
                start_vertex_bfs_levels = input("Enter starting vertex for BFS levels: ")
                graph.calculate_bfs_levels(start_vertex_bfs_levels)

            elif choice == 0:
                return

            else:
                OperationsGraph.deffault()

            input("Press Enter to continue...")

    @staticmethod
    def menu_graphs():
        while True:
            print("Types of graphs: \n"
                  + "1. Graph \n"
                  + "2. Directed graph \n"
                  + "0. Exit \n")

            try:
                opt = int(input())
            except ValueError:
                OperationsGraph.deffault()
                continue

            if opt == 1:
                OperationsGraph.all_operation_graph(Graph())
            elif opt == 2:
                OperationsGraph.all_operation_graph(DirectedGraph())
            elif opt == 0:
                return
            else:
                OperationsGraph.deffault()

    @staticmethod
    def deffault():
        input("Invalid input. Please enter a valid number.")
