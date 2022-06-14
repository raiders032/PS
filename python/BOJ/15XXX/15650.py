"""
https://www.acmicpc.net/problem/15650
15650번 N과 M (2)
실버3
풀이1.72ms
"""


def solve(index):
    if len(selected) == M:
        print(' '.join(map(str, selected)))
        return

    for i in range(index + 1, N + 1):
        selected.append(i)
        solve(i)
        selected.pop()


N, M = map(int, input().split())
selected = []
solve(0)
