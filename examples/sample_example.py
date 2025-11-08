import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from src import strongly_separates     


def unify_edges(edges: list[tuple[int, int]]):
    edges_set = set()

    for (vertex1, vertex2) in edges:
        if (vertex1, vertex2) in edges_set or (vertex2, vertex1) in edges_set:
            continue

    edges_set.add((vertex1, vertex2))

    return list(map(list, edges_set))

def build_system(edges: list[tuple[int, int]]):
    paths = []

    for (a, b) in edges:
        paths.append([a, b])

    return paths

if __name__ == "__main__":
    raw_edges = [(a, b) for a in range(4) for b in range (4) if a != b]
    K_4 = unify_edges(raw_edges)

    separating_path_system = build_system(K_4)
    print(separating_path_system)

    # “Checks whether the edge set of K_4 itself separates it.”
    strongly_separates(K_4, separating_path_system)