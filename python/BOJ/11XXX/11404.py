"""
https://www.acmicpc.net/problem/11404
11404.플로이드
풀이3
"""
import sys

input = sys.stdin.readline

V = int(input())
E = int(input())
distance = [[sys.maxsize] * (V + 1) for _ in range(V + 1)]
for i in range(V + 1):
    distance[i][i] = 0

for _ in range(E):
    vertex1, vertex2, weight = map(int, input().split())
    distance[vertex1][vertex2] = min(distance[vertex1][vertex2], weight)

for i in range(1, V + 1):
    for j in range(1, V + 1):
        for k in range(1, V + 1):
            if distance[j][i] + distance[i][k] < distance[j][k]:
                distance[j][k] = distance[j][i] + distance[i][k]

for row in distance[1:]:
    for d in row[1:]:
        if d == sys.maxsize:
            print('0', end=' ')
        else:
            print(d, end=' ')
    print()