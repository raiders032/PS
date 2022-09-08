"""
https://www.acmicpc.net/problem/1389
1389.케빈 베이컨의 6단계 법칙
풀이1.96ms
"""
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
min_distance = [[sys.maxsize] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    min_distance[v1][v2] = 1
    min_distance[v2][v1] = 1

for i in range(1, N + 1):
    min_distance[i][i] = 0

for i in range(1, N + 1):
    for x in range(1, N + 1):
        for y in range(1, N + 1):
            if min_distance[x][i] + min_distance[i][y] < min_distance[x][y]:
                min_distance[x][y] = min_distance[x][i] + min_distance[i][y]

min_bacon_count = sys.maxsize
answer = 0
for i in range(1, N + 1):
    bacon_count = sum(min_distance[i][1:])
    if bacon_count < min_bacon_count:
        min_bacon_count = bacon_count
        answer = i

print(answer)
