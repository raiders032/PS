"""
https://www.acmicpc.net/problem/1647
1647.도시 분할 계획
풀이1.3056ms
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
        disjoint_set[root1] = root2


N, M = map(int, input().split())
graph = []
disjoint_set = [i for i in range(N + 1)]
mst = []

for _ in range(M):
    v1, v2, w = map(int, input().split())
    graph.append((v1, v2, w))

graph.sort(key=lambda x: x[2])

for i in range(M):
    v1, v2, w = graph[i]
    if find(v1) == find(v2):
        continue
    mst.append(w)
    union(v1, v2)

mst.sort()
print(sum(mst) - max(mst))