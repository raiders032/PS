"""
https://www.acmicpc.net/problem/15652
15652.N과 M (4)
풀이2.56ms
"""
import sys
input = sys.stdin.readline
n, m = map(int, input().split())


def dfs(level, start, selected):
    if level == m:
        print(' '.join(map(str, selected)))
        return

    for i in range(start, n):
        dfs(level + 1, i, selected + [i + 1])


dfs(0, 0, [])