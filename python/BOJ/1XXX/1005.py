"""
https://www.acmicpc.net/problem/1005
1005.ACM Craft
골드3
풀이1.시간초과
"""
import sys
input = sys.stdin.readline


def get_max_time(vertex):
    if visited[vertex]:
        return visited[vertex]

    if len(graph[vertex]) == 0:
        visited[vertex] = times[vertex]
        return times[vertex]

    max_time = 0
    for i in range(len(graph[vertex])):
        max_time = max(max_time, times[vertex] + get_max_time(graph[vertex][i]))

    visited[vertex] = max_time
    return max_time


T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    times = [0] + list(map(int, input().split()))
    graph = [list() for _ in range(N + 1)]
    visited = [0] * (N + 1)
    for _ in range(K):
        v1, v2 = map(int, input().split())
        graph[v2].append(v1)

    W = int(input())
    print(get_max_time(W))