from pydsa.data_structures import DisjointSet
from typing import Any

def kruskal(edge_list: list[tuple[Any, Any, int]]) -> list[tuple[Any, Any, int]]:
    """Kruskal's algorithm to find the Minimum Spanning Forest (MSF) of a graph.
    
    Args:
        edge_list: A list of edges in the format (vertex1, vertex2, weight).
    
    Returns:
        A list of edges that form the Minimum Spanning Forest (MSF).
    """
    
    # Check edge_list is not empty
    if not edge_list:
        return []

    # Sort edges based on their weights
    sorted_edges = sorted(edge_list, key=lambda x: x[2])

    # Find unique vertices from the edge list
    vertices = set()
    for edge in edge_list:
        vertices.add(edge[0])
        vertices.add(edge[1])

    # Initialize Disjoint Set for the vertices
    disjoint_set = DisjointSet()

    for vertex in vertices:
        disjoint_set.make_set(vertex)
    
    mst_edges = []

    for edge in sorted_edges:
        vertex1, vertex2, weight = edge
        # Check if the vertices belong to different sets
        if disjoint_set.find(vertex1) != disjoint_set.find(vertex2):
            # If they are in different sets, include this edge in the MST
            mst_edges.append(edge)
            # Union the sets of the two vertices
            disjoint_set.union(vertex1, vertex2)
        
        if len(mst_edges) == len(vertices) - 1:
            break
    
    return mst_edges
