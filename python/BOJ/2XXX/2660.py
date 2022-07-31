"""
https://www.acmicpc.net/problem/2660
2660.회장뽑기
풀이1.84ms
"""
import sys

input = sys.stdin.readline
n = int(input())
min_distance = [[sys.maxsize] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    min_distance[i][i] = 0

while True:
    v1, v2 = map(int, input().split())
    if v1 == -1 and v2 == -1:
        break
    min_distance[v1][v2] = 1
    min_distance[v2][v1] = 1

for i in range(1, n + 1):
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            if min_distance[x][y] <= min_distance[x][i] + min_distance[i][y]:
                continue
            min_distance[x][y] = min_distance[x][i] + min_distance[i][y]

min_score = sys.maxsize
scores = [0]
for i in range(1, n + 1):
    scores.append(max(min_distance[i][1:]))
    min_score = min(min_score, scores[-1])

count = 0
answer_list = []
for i in range(1, n + 1):
    if min_score == scores[i]:
        count += 1
        answer_list.append(i)

print(min_score, count)
print(*answer_list)
