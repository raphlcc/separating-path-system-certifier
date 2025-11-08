from itertools import product


def edge_in_path(edge: tuple[str, str], path: list[str]) -> bool:
    """Checks whether a given edge is contained in a path.

    Args:
        edge (tuple[str, str]): A tuple representing an edge, e.g., ('u', 'v').
        path (list[str]): A list of vertex identifiers representing the path.

    Returns:
        bool: True if the edge appears (in either direction) in the path, False otherwise.
    """
    for index in range(len(path) - 1):
        path_edge = (path[index], path[index + 1])
        path_reverse_edge = (path[index + 1], path[index])

        if path_edge == edge or path_reverse_edge == edge:
            return True

    return False


def is_separated(
    edge1: tuple[str, str],
    edge2: tuple[str, str],
    separating_path_system: set[list[str]],
) -> bool:
    """Determines whether two edges are separated by a separating path system.

    An edge e1 is said to be separated from e2 if there exists a path in the
    separating path system that contains e1 but not e2.

    Args:
        edge1 (tuple[str, str]): The first edge.
        edge2 (tuple[str, str]): The second edge.
        separating_path_system (set[list[str]]): A set of paths, where each path
            is represented as a list of vertices.

    Returns:
        bool: True if there exists a path that separates edge1 from edge2,
        False otherwise.
    """
    for path in separating_path_system:
        if edge_in_path(edge1, path) and not edge_in_path(edge2, path):
            return True

    return False


def strongly_separates(
    edges: list[tuple[str, str]],
    separating_path_system: list[list[str]],
    verbose: bool = False,
) -> bool:
    """Checks whether a separating path system strongly separates all pairs of edges.

    A separating path system strongly separates the graph if, for every pair of
    distinct edges (e1, e2), there exists a path that separates e1 from e2 and
    another that separates e2 from e1.

    Args:
        edges (list[tuple[str, str]]): A list of edges, where each edge is a tuple of vertices.
        separating_path_system (list[list[str]]): A list of paths, where each path
            is represented as a list of vertices.
        verbose (bool, optional): If True, prints information about which edges are
            not separated. Defaults to False.

    Returns:
        bool: True if the system strongly separates all pairs of edges, False otherwise.
    """
    edge_pairs = product(edges, edges)
    separated = True

    for edge1, edge2 in edge_pairs:
        if edge1 == edge2 or is_separated(edge1, edge2, separating_path_system):
            continue

        separated = False
        if not verbose:
            break

        print(f"The edge {edge1} is not separated from {edge2}")

    if separated and verbose:
        print("The system separates the graph")

    return separated
