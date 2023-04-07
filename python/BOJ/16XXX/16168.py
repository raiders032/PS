"""
https://www.acmicpc.net/problem/16168
16168.퍼레이드
풀이1.52ms
"""
import sys

input = sys.stdin.readline
v, e = map(int, input().split())
graph = [list() for _ in range(v + 1)]
disjoint_set = [i for i in range(v + 1)]
degree = [0] * (v + 1)


def find(vertex):
    if disjoint_set[vertex] != vertex:
        disjoint_set[vertex] = find(disjoint_set[vertex])

    return disjoint_set[vertex]


def union(vertex1, vertex2):
    root1 = find(vertex1)
    root2 = find(vertex2)

    if root1 <= root2:
        disjoint_set[root2] = root1
    else:
        disjoint_set[root1] = root2


for _ in range(e):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
    union(v1, v2)
    degree[v1] += 1
    degree[v2] += 1

for vertex in range(1, v + 1):
    find(vertex)

if len(set(disjoint_set[1:])) != 1:
    print("NO")
    exit()

odd_count = 0
for d in degree[1:]:
    if d % 2 != 0:
        odd_count += 1

print("YES" if odd_count == 0 or odd_count == 2 else "NO")
