"""
https://www.acmicpc.net/problem/2110
2110.공유기 설치
실버1
풀이1.896ms
"""
import sys

input = sys.stdin.readline
N, C = map(int, input().split())
nums = [int(input()) for _ in range(N)]
nums.sort()
left = 1
right = nums[-1]
ans = 0

while left <= right:
    mid = (left + right) // 2
    count = 1
    start = 0
    end = 1
    while end < N:
        if nums[end] - nums[start] < mid:
            end += 1
            continue
        start = end
        end += 1
        count += 1

    if count < C:
        right = mid - 1
    else:
        left = mid + 1
        ans = mid

print(ans)
