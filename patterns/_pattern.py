from rdflib import Graph, IdentifiedNode


class Pattern:
    node_id: IdentifiedNode

    def to_graph(self) -> Graph:
        g = Graph()
        # translate this Python object to a Graph here
        return g
