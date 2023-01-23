"""
https://www.acmicpc.net/problem/7490
7490.0 만들기
풀이2.132ms
"""
import sys

input = sys.stdin.readline
answer = []


def dfs(level, expression):
    if level == n:
        if eval(expression.replace(" ", "")) != 0:
            return

        answer.append(expression)
        answer.append('\n')
        return

    dfs(level + 1, expression + " " + str(level + 1))
    dfs(level + 1, expression + "+" + str(level + 1))
    dfs(level + 1, expression + "-" + str(level + 1))


for _ in range(int(input())):
    n = int(input())
    dfs(1, "1")
    answer.append('\n')

print(''.join(answer))
