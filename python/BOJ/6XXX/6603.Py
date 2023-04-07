"""
https://www.acmicpc.net/problem/6603
6603.로또
실버2
백트래킹, 조합론, 재귀
풀이2.72ms
"""
import sys


def dfs(index, selected_numbers):
    if len(selected_numbers) == 6:
        print(*selected_numbers)
        return

    for i in range(index, len(array)):
        dfs(i + 1, selected_numbers + [array[i]])


input = sys.stdin.readline
while True:
    n, *array = list(map(int, input().split()))
    if n == 0:
        break
    dfs(0, [])
    print()
