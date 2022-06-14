"""
https://www.acmicpc.net/problem/15657
15657.N과 M (8)
실버3
풀이1.84ms
"""


def solve(index):
    if len(selected) == M:
        print(' '.join(map(str, selected)))
        return

    for i in range(index, N):
        selected.append(numbers[i])
        solve(i)
        selected.pop()


N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
selected = []
solve(0)