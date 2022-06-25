"""
https://www.acmicpc.net/problem/17208
17208.카우버거 알바생
골드4
풀이1.시간초과
"""
import sys
input = sys.stdin.readline


def solve(level):
    global answer, M, K
    answer = max(answer, len(selected))

    if level == N:
        return

    if orders[level][0] <= M and orders[level][1] <= K:
        selected.append(level)
        M -= orders[level][0]
        K -= orders[level][1]
        solve(level + 1)
        selected.pop()
        M += orders[level][0]
        K += orders[level][1]

    solve(level + 1)


N, M, K = map(int, input().split())
orders = [tuple(map(int, input().split())) for _ in range(N)]
selected = []
answer = 0
solve(0)
print(answer)