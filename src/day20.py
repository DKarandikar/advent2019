from collections import defaultdict
from typing import Tuple

import numpy as np

from src.inputHelpers.text_grids import parse_text_grid_to_numpy_array
from src.logicHelpers.graph import Graph


def createGraph(data: np.array) -> Tuple[Graph, Tuple[int, int], Tuple[int, int]]:
    g = Graph()
    teleports = defaultdict(list)

    for x in range(data.shape[0]):
        for y in range(data.shape[1]):
            if data[x, y] == ".":
                for a, b in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                    if data[x+a, y+b] == ".":
                        g.addEdge((x, y), (x+a, y+b))
                        g.addEdge((x + a, y + b), (x, y))
                    elif data[x+a, y+b] not in (".", "#", " "):
                        teleportName = sorted([data[x + a + a, y + b + b], data[x + a, y + b]])
                        teleports[tuple(teleportName)].append((x, y))

    for key, teleport in teleports.items():
        if len(teleport) == 2:
            g.addEdge(teleport[0], teleport[1])
            g.addEdge(teleport[1], teleport[0])
        elif len(teleport) == 1:
            # start or end
            pass
        else:
            raise RuntimeError(f"Too many points for teleport: {key}")

    return g, teleports.get(("A", "A"))[0], teleports.get(("Z", "Z"))[0]


def get_shortest_distance_start_to_end(filename: str):
    data = parse_text_grid_to_numpy_array(filename)
    g, start, end = createGraph(data)
    return len(g.BFS(start, end).history)


def main():
    part1 = get_shortest_distance_start_to_end(".././inputData/day20part1")
    print(f"Part 1 shortest is {part1}")


if __name__ == "__main__":
    main()