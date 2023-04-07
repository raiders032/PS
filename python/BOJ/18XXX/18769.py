"""
https://www.acmicpc.net/problem/18769
18769.그리드 네트워크
풀이1.6216ms(PyPy3)
"""
import sys

input = sys.stdin.readline


def find(node):
    if disjoint_set[node] != node:
        disjoint_set[node] = find(disjoint_set[node])

    return disjoint_set[node]


def union(node1, node2):
    root1 = find(node1)
    root2 = find(node2)

    if root1 <= root2:
        disjoint_set[root2] = root1
    else:
        disjoint_set[root2] = root1


for _ in range(int(input())):
    R, C = map(int, input().split())
    edge = []
    disjoint_set = [i for i in range(R * C)]
    sheep_count = 0

    for r in range(R):
        weights = map(int, input().split())
        for index, weight in enumerate(weights):
            edge.append((weight, r * C + index, r * C + index + 1))

    for r in range(R - 1):
        weights = map(int, input().split())
        for index, weight in enumerate(weights):
            edge.append((weight, r * C + index, r * C + index + C))

    edge.sort()

    for weight, vertex1, vertex2 in edge:
        if find(vertex1) == find(vertex2):
            continue
        union(vertex1, vertex2)
        sheep_count += weight

    print(sheep_count)