"""
https://www.acmicpc.net/problem/7785
7785.회사에 있는 사람
실버5
풀이1.240ms
"""
import sys

input = sys.stdin.readline
N = int(input())
workers = set()
for _ in range(N):
    name, enter = input().rstrip().split()
    if enter == 'enter':
        workers.add(name)
    else:
        workers.remove(name)
for name in sorted(workers, reverse=True):
    print(name)
