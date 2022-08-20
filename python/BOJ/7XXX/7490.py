"""
https://www.acmicpc.net/problem/7490
7490.0 만들기
풀이1.160ms
"""
import sys
input = sys.stdin.readline


def dfs(level, exp):
    if level == N:
        if eval(exp.replace(" ", "")) == 0:
            print(exp)
        return

    dfs(level + 1, exp + " " + str(level + 1))
    dfs(level + 1, exp + "+" + str(level + 1))
    dfs(level + 1, exp + "-" + str(level + 1))


for _ in range(int(input())):
    N = int(input())
    dfs(1, "1")
    print()
