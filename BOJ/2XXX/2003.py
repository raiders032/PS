"""
https://www.acmicpc.net/problem/2003
2003.수들의 합 2
실버3
두포인터
풀이1.80ms
"""
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
left = 0
right = 0
sum = arr[0]
res = 0

while right < N:
    if sum == M:
        res += 1
        right += 1
        if right >= N:
            break
        sum += arr[right]
        sum -= arr[left]
        left += 1
    elif sum > M:
        sum -= arr[left]
        left += 1
    elif sum < M:
        right += 1
        if right >= N:
            break
        sum += arr[right]
print(res)
