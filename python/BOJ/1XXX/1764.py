"""
https://www.acmicpc.net/problem/1764
1764.듣보잡
실버4
풀이1.140ms
"""
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
names = set()
dbj = []
for _ in range(N + M):
    name = input().rstrip()
    if name in names:
        dbj.append(name)
    else:
        names.add(name)
dbj.sort()
print(len(dbj))
for name in dbj:
    print(name)