import sys

N = int(sys.stdin.readline())
graph = [[sys.maxsize] * N for _ in range(N)]
scores = [0] * N
cnt = 0
for i in range(N):
    graph[i][i] = 0
while True:
    v1, v2 = map(int, sys.stdin.readline().split())
    if v1 == -1 and v2 == -1:
        break
    graph[v1 - 1][v2 - 1] = 1

for i in range(N):
    for r in range(N):
        for c in range(N):
            graph[r][c] = min(graph[r][c], graph[r][i] + graph[i][c])

for r in range(N):
    for c in range(N):
        scores[r] = max(scores[r], graph[r][c])

min_score = min(scores)
print(min_score, scores.count(min_score))
for x in scores:
    if x == min_score:
        print(x, end=' ')
