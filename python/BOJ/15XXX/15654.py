"""
https://www.acmicpc.net/problem/15654
15654.N과 M (5)
실버3
풀이1.204ms
"""
import sys
input = sys.stdin.readline


def solve():
    if len(selected) == M:
        print(' '.join(map(str, selected)))
        return

    for i in range(1, N + 1):
        if visited[i]:
            continue
        selected.append(numbers[i - 1])
        visited[i] = True
        solve()
        selected.pop()
        visited[i] = False


N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
visited = [False] * (N + 1)
selected = []
solve()