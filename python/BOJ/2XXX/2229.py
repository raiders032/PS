"""
https://www.acmicpc.net/problem/2229
2229.조 짜기
풀이1.5692ms
"""
import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
dp = [0] * n

for i in range(1, n):
    for j in range(i + 1):
        min_number = min(numbers[j:i + 1])
        max_number = max(numbers[j:i + 1])
        dp[i] = max(dp[i], dp[j - 1] + max_number - min_number)

print(dp[n - 1])
