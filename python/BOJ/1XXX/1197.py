"""
https://www.acmicpc.net/problem/1197
1197.최소 스패닝 트리
풀이1.404ms
"""
import sys


def find(node):
    if disjoint_set[node] != node:
        disjoint_set[node] = find(disjoint_set[node])
    return disjoint_set[node]


def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a <= root_b:
        disjoint_set[root_b] = root_a
    else:
        disjoint_set[root_a] = root_b


input = sys.stdin.readline
V, E = map(int, input().split())
graph = []
for _ in range(E):
    v1, v2, w = map(int, input().split())
    graph.append((w, v1, v2))
graph.sort()
disjoint_set = [i for i in range(V + 1)]
sheep_count = 0

for i in range(E):
    weight, vertex1, vertex2 = graph[i]
    if find(vertex1) == find(vertex2):
        continue
    union(vertex1, vertex2)
    sheep_count += weight

print(sheep_count)
