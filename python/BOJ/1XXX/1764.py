"""
https://www.acmicpc.net/problem/1764
1764.듣보잡
실버4
풀이2.116ms
"""
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
names = set()
result = []

for _ in range(N):
    names.add(input().rstrip())

for _ in range(M):
    name = input().rstrip()
    if name in names:
        result.append(name)

print(len(result))
for name in sorted(result):
    print(name)