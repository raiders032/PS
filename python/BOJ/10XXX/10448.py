"""
https://www.acmicpc.net/problem/10448
10448.유레카 이론
브론즈2
풀이1.
"""
import sys

input = sys.stdin.readline
nums = [n * (n + 1) // 2 for n in range(1, 45)]
is_possible = set()
for i in range(len(nums)):
    for j in range(len(nums)):
        for k in range(len(nums)):
            is_possible.add(nums[i] + nums[j] + nums[k])

N = int(input())
for _ in range(N):
    if int(input()) in is_possible:
        print(1)
    else:
        print(0)
