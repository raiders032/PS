"""
https://www.acmicpc.net/problem/17390
17390.이건 꼭 풀어야 해!
풀이1.760ms
"""
import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
numbers = [0] + sorted(list(map(int, input().split())))
prefix_sum = [0] * (N + 1)
prefix_sum[1] = numbers[1]
for i in range(2, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + numbers[i]

for _ in range(Q):
    start, end = map(int, input().split())
    print(prefix_sum[end] - prefix_sum[start - 1])
