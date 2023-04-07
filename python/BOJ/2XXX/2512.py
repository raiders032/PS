"""
https://www.acmicpc.net/problem/2512
2512.예산
실버3
풀이2
"""


def is_possible(limit):
    total_budge = 0
    for b in budget:
        if b < limit:
            total_budge += b
        else:
            total_budge += limit
    if total_budge <= total:
        return True
    else:
        return False


N = int(input())
budget = list(map(int, input().split()))
total = int(input())
left = 0
right = max(budget)
ans = 0

while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        left = mid + 1
        ans = mid
    else:
        right = mid - 1

print(ans)
