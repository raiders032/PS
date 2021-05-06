"""
https://www.acmicpc.net/problem/1182
1182.부분수열의 합
실버2
풀이1.452ms
"""
import sys


def dfs(level, sum, count):
    if level == len(array):
        if sum == S and count:
            return 1
        return 0
    return dfs(level + 1, sum + array[level], count + 1) + dfs(level + 1, sum, count)



input = sys.stdin.readline
N, S = map(int, input().split())
array = list(map(int, input().split()))
print(dfs(0, 0, 0))
