"""
https://www.acmicpc.net/problem/1922
1922.네트워크 연결
풀이1.332ms
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


V = int(input())
E = int(input())
edge = []
disjoint_set = [i for i in range(V + 1)]
for _ in range(E):
    vertex1, vertex2, weight = map(int, input().split())
    edge.append((weight, vertex1, vertex2))

edge.sort()
sheep_count = 0
for weight, vertex1, vertex2 in edge:
    if find(vertex1) == find(vertex2):
        continue
    union(vertex1, vertex2)
    sheep_count += weight

print(sheep_count)

