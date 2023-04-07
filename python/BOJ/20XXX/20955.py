"""
https://www.acmicpc.net/problem/20955
20955.민서의 응급 수술
풀이1.244ms
"""
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
roots = [i for i in range(n)]
answer = 0


def find(vertex):
    if roots[vertex] != vertex:
        roots[vertex] = find(roots[vertex])

    return roots[vertex]


def union(vertex1, vertex2):
    root1 = find(vertex1)
    root2 = find(vertex2)

    if root1 <= root2:
        roots[root2] = root1
    else:
        roots[root1] = root2


for _ in range(m):
    vertex1, vertex2 = map(lambda x: int(x) - 1, input().split())

    if find(vertex1) == find(vertex2):
        answer += 1
        continue

    union(vertex1, vertex2)

for i in range(n):
    find(i)

answer += len(set(roots)) - 1
print(answer)
