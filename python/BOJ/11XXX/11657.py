"""
https://www.acmicpc.net/problem/11657
11657.타임머신
풀이1.1284ms
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
distance = [sys.maxsize] * (n + 1)
distance[1] = 0
is_cycle = False
edges = [tuple(map(int, input().split())) for _ in range(m)]

for _ in range(n - 1):
    for edge in edges:
        (v1, v2, cost) = edge
        if distance[v1] == sys.maxsize:
            continue

        if distance[v1] + cost < distance[v2]:
            distance[v2] = distance[v1] + cost

for edge in edges:
    (v1, v2, cost) = edge
    if distance[v1] == sys.maxsize:
        continue

    if distance[v1] + cost < distance[v2]:
        is_cycle = True
        break

if is_cycle:
    print("-1")
else:
    answer = []
    for d in distance[2:]:
        if d == sys.maxsize:
            answer.append("-1")
        else:
            answer.append(str(d))
    print("\n".join(answer))
