"""
https://www.acmicpc.net/problem/17073
17073.나무 위의 빗물
풀이1.696ms
"""
import sys

input = sys.stdin.readline

N, W = map(int, input().split())
degree = [0] * (N + 1)
for _ in range(N - 1):
    v1, v2 = map(int, input().split())
    degree[v1] += 1
    degree[v2] += 1

leaf_count = 0
for i in range(2, N + 1):
    if degree[i] == 1:
        leaf_count += 1

print(W / leaf_count)