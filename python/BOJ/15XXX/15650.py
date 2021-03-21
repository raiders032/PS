"""
15650번 N과 M (2) 실버3
백트래킹
"""
N, M = map(int, input().split())
selected = []


def dfs(level, idx):
    if level == M:
        for x in selected:
            print(x, end=' ')
        print()
        return
    else:
        for i in range(idx, N):
            selected.append(i+1)
            dfs(level+1, i+1)
            selected.pop()


dfs(0, 0)
