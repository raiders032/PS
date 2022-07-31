"""
https://www.acmicpc.net/problem/15654
15654.N과 M (5)
풀이2.244ms
"""
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
visited_index = [False] * n
numbers = sorted(list(map(int, input().split())))
selected = []


def select(level):
    if level == m:
        print(*selected)
        return

    for i in range(n):
        if visited_index[i]:
            continue
        visited_index[i] = True
        selected.append(numbers[i])
        select(level + 1)
        selected.pop()
        visited_index[i] = False


select(0)