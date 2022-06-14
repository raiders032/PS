"""
https://www.acmicpc.net/problem/15652
15652.N과 M (4)
실버3
풀이1.76ms
"""


def solve(index):
    if len(selected) == M:
        print(' '.join(map(str, selected)))
        return
    for i in range(index, N + 1):
        selected.append(i)
        solve(i)
        selected.pop()


N, M = map(int, input().split())
selected = []
solve(1)