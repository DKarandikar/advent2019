from dataclasses import dataclass, field
from queue import Queue
from typing import TypeVar, List, Dict

T = TypeVar("T")


@dataclass
class Node:
    label: T
    history: List[T] = field(default_factory=list)
    edges: List['Node'] = field(default_factory=list)
    visited: bool = False


class Graph:
    def __init__(self):
        self.graph: Dict[T, Node] = {}

    def addEdge(self, u: T, v: T):
        nodeU = self.graph.get(u)
        if not nodeU:
            self.graph[u] = Node(u)
        nodeV = self.graph.get(v, Node(v))
        self.graph[u].edges.append(nodeV)

    def BFS(self, start: T, end: T):
        for node in self.graph.values():
            node.visited = False

        queue: Queue[Node] = Queue()
        queue.put(self.graph[start])
        self.graph[start].visited = True

        while queue:
            s = queue.get()
            if s.label == end:
                return s

            for i in s.edges:
                if not i.visited:
                    queue.put(i)
                    i.visited = True
                    i.history = s.history + [s.label]

# g = Graph()
# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(1, 2)
# g.addEdge(2, 0)
# g.addEdge(2, 3)
# g.addEdge(3, 3)
# 
# print("Following is Breadth First Traversal"
#       " (starting from vertex 2)")
# print(g.BFS(2, 1))
