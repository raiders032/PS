"""
https://www.acmicpc.net/problem/14002
14002. 가장 긴 증가하는 부분 수열 4
골드4
다이나믹프로그래밍
풀이1.172ms
"""
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [(1, 0) for _ in range(N)]
max_len, max_idx = 1, 0
lis = []
for cur in range(1, N):
    for pre in range(cur):
        if arr[pre] < arr[cur] and dp[cur][0] < dp[pre][0] + 1:
            dp[cur] = (dp[pre][0] + 1, pre)
            if max_len < dp[cur][0]:
                max_len = dp[cur][0]
                max_idx = cur

while max_idx:
    lis.append(arr[max_idx])
    max_idx = dp[max_idx][1]
lis.append(arr[max_idx])

print(max_len)
for i in range(max_len - 1, -1, -1):
    print(lis[i], end=' ')
