"""
https://www.acmicpc.net/problem/14225
14225.부분수열의 합
실버1
브루트포스
풀이1.628ms
"""
import sys


def bfs(lv, sum):
    if lv == N:
        check.add(sum)
        return
    bfs(lv + 1, sum + arr[lv])
    bfs(lv + 1, sum)


input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
check = set()

bfs(0, 0)
for i in range(1, len(check) + 1):
    if i not in check:
        print(i)
        break
