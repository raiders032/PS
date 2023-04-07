"""
https://www.acmicpc.net/problem/2212
2212.센서
골드5
풀이2.72ms
"""
N = int(input())
K = int(input())
nums = list(map(int, input().split()))
nums.sort()

diff = []
for i in range(1, N):
    diff.append(nums[i] - nums[i - 1])
diff.sort(reverse=True)
print(sum(diff[K - 1:]))