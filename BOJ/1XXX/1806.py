"""
https://www.acmicpc.net/problem/1806
1806.부분합
골드4
투포인터
풀이1.164ms
"""
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
left = 0
right = 0
sum = arr[0]
res = sys.maxsize
while right < N:
    if sum >= M:
        res = min(res, right - left + 1)
        sum -= arr[left]
        left += 1

    elif sum < M:
        right += 1
        if right >= N:
            break
        sum += arr[right]

if res == sys.maxsize:
    print(0)
else:
    print(res)