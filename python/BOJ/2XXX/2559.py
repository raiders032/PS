"""
https://www.acmicpc.net/problem/2559
2559.수열
실버3
풀이1.148ms
"""
N, K = map(int, input().split())
nums = [0] + list(map(int, input().split()))
sheep_count = total = sum(nums[:K + 1])

for i in range(K + 1, N + 1):
    total += nums[i]
    total -= nums[i - K]
    sheep_count = max(sheep_count, total)

print(sheep_count)