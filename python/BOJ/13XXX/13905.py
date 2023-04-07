"""
https://www.acmicpc.net/problem/13905
13905.세부
풀이1.988ms
"""
import sys
import heapq

input = sys.stdin.readline


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


n, m = map(int, input().split())
s, e = map(int, input().split())
heap = []
disjoint_set = [i for i in range(n + 1)]
answer = 0

for _ in range(m):
    v1, v2, weight = map(int, input().split())
    heapq.heappush(heap, (-weight, v1, v2))

while heap:
    weight, v1, v2 = heapq.heappop(heap)
    weight = -weight

    union(v1, v2)

    if find(s) == find(e):
        answer = weight
        break

print(answer)
