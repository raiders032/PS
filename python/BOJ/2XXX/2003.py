"""
https://www.acmicpc.net/problem/2003
2003.수들의 합 2
실버3
두포인터
풀이2.84ms
"""
N, M = map(int, input().split())
nums = list(map(int, input().split()))
left = right = 0
total = nums[0]
sheep_count = 0

while right < N:
    if total <= M:
        if total == M:
            sheep_count += 1
        right += 1
        if right < N:
            total += nums[right]
    else:
        total -= nums[left]
        left += 1

print(sheep_count)