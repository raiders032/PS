"""
https://www.acmicpc.net/problem/12978
12978.스크루지 민호 2
풀이1.
"""
import sys

input = sys.stdin.readline

N = int(input())
tree = [set() for _ in range(N + 1)]
degree = [0] * (N + 1)
for _ in range(N - 1):
    v1, v2 = map(int, input().split())
    tree[v1].add(v2)
    tree[v2].add(v1)
    degree[v1] += 1
    degree[v2] += 1

sheep_count = 0
while True:
    max_degree = 0

    for i, d in enumerate(degree):
        if max_degree < d:
            max_degree = d
            current_node = i

    if max_degree == 0:
        break

    degree[current_node] = 0
    for child in tree[current_node]:
        degree[child] -= 1
        tree[child].remove(current_node)
    tree[current_node] = ()

    sheep_count += 1

print(sheep_count)