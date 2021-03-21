"""
https://www.acmicpc.net/problem/14002
14002. 가장 긴 증가하는 부분 수열 4
골드4
다이나믹프로그래밍
풀이2.168ms
"""
import sys

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
dp = [1] * N
parent = [-1] * N

for current_index in range(1, N):
    for pre_index in range(0, current_index):
        if arr[current_index] <= arr[pre_index]:
            continue
        if dp[current_index] < dp[pre_index] + 1:
            dp[current_index] = dp[pre_index] + 1
            parent[current_index] = pre_index

index = dp.index(max(dp))
length = dp[index]
lis = []
while parent[index] != -1:
    lis.append(arr[index])
    index = parent[index]
lis.append(arr[index])
print(length)
print(*lis[::-1])