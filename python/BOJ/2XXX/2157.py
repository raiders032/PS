"""
https://www.acmicpc.net/problem/2157
2157.여행
골드4
풀이1.2084ms
"""
import sys
import collections
input = sys.stdin.readline


def solve():
    q = collections.deque()
    q.append((1, 1))

    while q:
        count, vertex = q.popleft()
        if count == M:
            continue

        for next_vertex, weight in graph[vertex]:
            if visited[vertex][count] + weight <= visited[next_vertex][count + 1]:
                continue

            visited[next_vertex][count + 1] = visited[vertex][count] + weight
            q.append((count + 1, next_vertex))


N, M, K = map(int, input().rstrip().split())
graph = collections.defaultdict(list)
visited = [[0] * 301 for _ in range(N + 1)]
for _ in range(K):
    v1, v2, w = map(int, input().rstrip().split())
    if v1 > v2:
        continue
    graph[v1].append((v2, w))
solve()
print(max(visited[N]))