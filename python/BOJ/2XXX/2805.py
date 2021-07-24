"""
https://www.acmicpc.net/problem/2805
2805.나무 자르기
실버3
풀이1.3728ms
"""
N, M = map(int, input().split())
heights = list(map(int, input().split()))
left = 0
right = max(heights)
ans = 0


def is_possible(height):
    total = 0
    for h in heights:
        total += h - height if h - height >= 0 else 0

    if total >= M:
        return True
    else:
        return False


while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        left = mid + 1
        ans = mid
    else:
        right = mid - 1
print(ans)