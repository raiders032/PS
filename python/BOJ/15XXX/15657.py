"""
https://www.acmicpc.net/problem/15657
15657.N과 M (8)
풀이2.92ms
"""
import sys
input = sys.stdin.readline


def select(level):
    if len(selected) == M:
        print(*selected)
        return

    for i in range(level, N):
        selected.append(numbers[i])
        select(i)
        selected.pop()


N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
selected = []
select(0)