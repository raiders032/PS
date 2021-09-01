"""
https://www.acmicpc.net/problem/2428
2428.표절
실버3
풀이1.880ms
"""
N = int(input())
files = list(map(int, input().split()))
files.sort(reverse=True)
answer = 0

for i in range(N):
    left = i + 1
    right = N - 1
    index = 0

    while left <= right:
        mid = (left + right) // 2
        if files[mid] >= 0.9 * files[i]:
            left = mid + 1
            index = mid
        else:
            right = mid - 1

    answer += index - i if index else 0

print(answer)