"""
https://www.acmicpc.net/problem/15655
15655.N과 M (6)
풀이1.72ms
"""
N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
selected = []


def dfs(level, index):
    if level == M:
        for number in selected:
            print(number, end=' ')
        print()
        return

    for i in range(index, N):
        selected.append(numbers[i])
        dfs(level + 1, i + 1)
        selected.pop()


dfs(0, 0)