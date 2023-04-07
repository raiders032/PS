"""
https://www.acmicpc.net/problem/7785
7785.회사에 있는 사람
실버5
풀이2.244ms
"""
import sys

input = sys.stdin.readline
workers = set()
for _ in range(int(input())):
    name, enter_or_leave = input().rstrip().split()
    if enter_or_leave == 'enter':
        workers.add(name)
    else:
        workers.discard(name)

for name in sorted(workers, reverse=True):
    print(name)