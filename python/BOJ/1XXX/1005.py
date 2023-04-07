"""
https://www.acmicpc.net/problem/1005
1005.ACM Craft
골드3
풀이2
"""
import sys, collections

input = sys.stdin.readline


def topology_sort(W):
    max_times = [0] * (N + 1)
    q = collections.deque()

    for i in range(1, N + 1):
        if in_degree[i] == 0:
            q.append(i)
            max_times[i] = times[i]

    while True:
        if not in_degree[W]:
            return max_times[W]

        vertex = q.popleft()
        for w in graph[vertex]:
            in_degree[w] -= 1
            max_times[w] = max(max_times[w], max_times[vertex] + times[w])
            if in_degree[w] == 0:
                q.append(w)


T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    times = [0] + list(map(int, input().split()))
    in_degree = [0] * (N + 1)
    graph = [list() for _ in range(N + 1)]
    for _ in range(K):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        in_degree[v2] += 1

    W = int(input())
    print(topology_sort(W))