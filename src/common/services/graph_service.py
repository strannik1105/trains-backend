import networkx as networkx
from networkx import Graph
from models.stations import Route
import matplotlib.pyplot as plt


class GraphService:
    _graph: Graph = None

    @classmethod
    def create_graph(cls, routes: list[Route]):
        cls._graph = networkx.Graph()

        for route in routes:
            cls._graph.add_edge(route.node1_sid, route.node2_sid, weight=route.length)

    @classmethod
    def is_way_exist(cls, first_node: int, second_node: int) -> bool:
        if first_node in cls._graph and second_node in cls._graph:
            return networkx.has_path(cls._graph, first_node, second_node)

        return False

    @classmethod
    def shortest_path(cls, first_node: int, second_node: int) -> list:
        return networkx.shortest_path(cls._graph, first_node, second_node)

    @classmethod
    def length_of_path(cls, first_node: int, second_node: int):
        return networkx.dijkstra_path_length(cls._graph, first_node, second_node)

    @classmethod
    def all_shortest_paths(cls, first_node: int, second_node: int):
        return networkx.all_shortest_paths(cls._graph, first_node, second_node)

    @classmethod
    def all_simple_paths(cls, first_node: int, second_node: int):
        return networkx.all_simple_paths(cls._graph, first_node, second_node)

    @classmethod
    def print_graph(cls):
        networkx.draw(cls._graph, with_labels=True)
        plt.show()
