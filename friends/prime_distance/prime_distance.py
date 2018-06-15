"""
best practices:
1- give minor hints when stuck
2- write down ANY comment you think of (mostly bad, but also good)
3- take time (11:07 - solved riddle. 11:10 - can't sketch out code but not relenting. 11:15: samba party)
"""
from collections import deque
from itertools import combinations
from typing import Set, Tuple, Deque


# two num 4 digits, prime,
# what's the shortest "path" between them,
#### Gran solution ####
# calculate {all-primes}
# represent the source, primes and target as a graph
# find shortest path
# Tasks: 1) make it run, 2)
# Notes: know BFS by-heart. Know DS APIs


class Node:
    def __init__(self, value, neighbors=None):
        self.value = value
        self.neighbors = set() if neighbors is None else neighbors  # TODO in prod: restrict access etc

    def __repr__(self):
        return f'Node({self.value},{[n.value for n in self.neighbors]})'


def find_shortest_prime_path(x: int, y: int):
    x_str = str(x)
    y_str = str(y)

    primes: Set[str] = all_primes()
    source, target = create_graph(x_str, y_str, primes)
    return bfs_distance(source, target)


def bfs_distance(source: Node, target: Node):
    if source.value == target.value:
        return 0

    queue = deque()  # type: Deque[Tuple[Node, int]]
    visited = {source.value}

    queue.extendleft([(n, 1) for n in source.neighbors])

    while len(queue) > 0:
        current, dist = queue.pop()
        if current.value == target.value:
            return dist

        visited.add(current.value)
        to_visit_neighbors = [(n, dist + 1) for n in current.neighbors if n.value not in visited]
        queue.extendleft(to_visit_neighbors)


def all_primes() -> Set[str]:
    return {str(x) for x in range(1000, 10000) if is_prime(x)}


def is_prime(x):
    return all(x % n != 0 for n in range(2, int(x ** 0.5) + 1))


def create_graph(x: str, y: str, primes: Set[str]) -> Tuple[Node, Node]:
    nodes = {Node(v) for v in primes}
    for n1, n2 in combinations(nodes, 2):
        if word_distance(n1.value, n2.value) == 1:
            n1.neighbors.add(n2)  # RON COMMENT - whats the SET interface?
            n2.neighbors.add(n1)
    return next(node for node in nodes if str(node.value) == x), next(node for node in nodes if str(node.value) == y)


def word_distance(x: str, y: str):  # assume |x| == |y|
    difference = 0
    for x_c, y_c in zip(x, y):
        if x_c != y_c:
            difference += 1  # TODO - rewrite more pythonic
    return difference


if __name__ == '__main__':
    print(sorted(list(all_primes())))
    assert find_shortest_prime_path(1013, 1019) == 1, find_shortest_prime_path(1013, 1019)
    assert find_shortest_prime_path(1033, 1039) == 1
    assert find_shortest_prime_path(1009, 1109) == 1
    assert find_shortest_prime_path(1019, 1129) == 2, find_shortest_prime_path(1019, 1129)
