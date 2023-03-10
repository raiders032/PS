"""
https://www.acmicpc.net/problem/14225
14225.부분수열의 합
풀이2.680ms
"""
import sys


def dfs(level, sum):
    if level == len(array):
        sum_set.add(sum)
        return
    dfs(level + 1, sum + array[level])
    dfs(level + 1, sum)


sum_set = set()
input = sys.stdin.readline
N = int(input())
array = list(map(int, input().split()))
dfs(0, 0)
sheep_count = 1
while True:
    if sheep_count not in sum_set:
        print(sheep_count)
        break
    sheep_count += 1

