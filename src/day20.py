from collections import defaultdict
from typing import Tuple

import numpy as np
import networkx as nx

from src.inputHelpers.text_grids import parse_text_grid_to_numpy_array


def createGraphPart1(data: np.array) -> Tuple[nx.Graph, Tuple[int, int], Tuple[int, int]]:
    g = nx.Graph()
    teleports = defaultdict(list)
    edges, extTeleports, intTeleports = get_edges_and_portals(data)

    for teleportCode, location in extTeleports.items():
        teleports[teleportCode].append(location)
    for teleportCode, location in intTeleports.items():
        teleports[teleportCode].append(location)

    for edgePair in edges:
        g.add_edge(edgePair[0], edgePair[1])

    for key, teleport in teleports.items():
        if len(teleport) == 2:
            g.add_edge(teleport[0], teleport[1])
            g.add_edge(teleport[1], teleport[0])
        elif len(teleport) == 1:
            # start or end
            pass
        else:
            raise RuntimeError(f"Too many points for teleport: {key}")

    return g, teleports.get(("A", "A"))[0], teleports.get(("Z", "Z"))[0]


def createGraphPart2(data: np.array) -> Tuple[nx.Graph, Tuple[int, int], Tuple[int, int]]:
    g = nx.Graph()
    edges, extTeleports, intTeleports = get_edges_and_portals(data)

    for layer in range(500):
        for edgePair in edges:
            g.add_edge((*edgePair[0], layer), (*edgePair[1], layer))

        for name, location in intTeleports.items():
            g.add_edge((*location, layer), (*extTeleports.get(name), layer + 1))

        for name, location in extTeleports.items():
            if layer != 0 and name != ("A", "A") and name != ("Z", "Z"):
                g.add_edge((*location, layer), (*intTeleports.get(name), layer - 1))

    return g, (*extTeleports.get(("A", "A")), 0), (*extTeleports.get(("Z", "Z")), 0)


def get_edges_and_portals(data):
    intTeleports = {}
    extTeleports = {}
    width = data.shape[0]
    height = data.shape[1]
    edges = []
    for x in range(width):
        for y in range(height):
            if data[x, y] == ".":
                for a, b in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                    neighbour_element = data[x + a, y + b]
                    if neighbour_element == ".":
                        edges.append(((x, y), (x + a, y + b)))
                        edges.append(((x + a, y + b), (x, y)))
                    elif neighbour_element not in (".", "#", " "):
                        # It's a letter
                        furthest_letter_x = x + 2 * a
                        furthest_letter_y = y + 2 * b
                        furthest_letter = data[furthest_letter_x, furthest_letter_y]
                        teleportName = tuple(sorted([furthest_letter, neighbour_element]))
                        if furthest_letter_x in (0, width - 1) or furthest_letter_y in (0, height - 1):
                            extTeleports[teleportName] = (x, y)
                        else:
                            intTeleports[teleportName] = (x, y)
    return edges, extTeleports, intTeleports


def get_shortest_distance_start_to_end(filename: str):
    data = parse_text_grid_to_numpy_array(filename)
    g, start, end = createGraphPart1(data)
    rv = nx.shortest_path(g, source=start, target=end)
    return len(rv) - 1


def get_shortest_distance_start_to_end_layers(filename: str):
    data = parse_text_grid_to_numpy_array(filename)
    g, start, end = createGraphPart2(data)
    rv = nx.shortest_path(g, source=start, target=end)
    return len(rv) - 1


def main():
    part1 = get_shortest_distance_start_to_end(".././inputData/day20part1")
    print(f"Part 1 shortest is {part1}")
    part2 = get_shortest_distance_start_to_end_layers(".././inputData/day20part1")
    print(f"Part 2 shortest is {part2}")


if __name__ == "__main__":
    main()
