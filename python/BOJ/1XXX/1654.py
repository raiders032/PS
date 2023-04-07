"""
https://www.acmicpc.net/problem/1654
1654.랜선 자르기
풀이4.132ms
"""
import sys

input = sys.stdin.readline


def decision_problem(length):
    wire_count = 0
    for w in wire:
        wire_count += w // length
    return wire_count >= N


K, N = map(int, input().split())
wire = [int(input()) for _ in range(K)]

low = 0
high = 2 ** 31
while low + 1 < high:
    mid = (low + high) // 2
    if decision_problem(mid) == decision_problem(high):
        high = mid
    else:
        low = mid
print(low)
