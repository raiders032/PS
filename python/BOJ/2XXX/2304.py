"""
https://www.acmicpc.net/problem/2304
2304.창고 다각형
실버2
풀이1.68ms
"""
import sys

input = sys.stdin.readline
N = int(input())

arr = list()
max_height =0
middle = 0

for i in range(N):
    x, y = map(int, input().split())
    arr.append((x, y))
arr.sort(key=lambda l: l[0])

for i in range(N):
    if max_height < arr[i][1]:
        max_height = arr[i][1]
        middle = i

ans = max_height
stack = []
for i in range(middle + 1):
    if not stack:
        stack.append((arr[i][0], arr[i][1]))
    else:
        if stack[-1][1] <= arr[i][1]:
            ans += (arr[i][0] - stack[-1][0]) * stack[-1][1]
            stack.append((arr[i][0], arr[i][1]))

stack = []
for i in range(N - 1, middle - 1, -1):
    if not stack:
        stack.append((arr[i][0], arr[i][1]))
    else:
        if stack[-1][1] <= arr[i][1]:
            ans += (stack[-1][0] - arr[i][0]) * stack[-1][1]
            stack.append((arr[i][0], arr[i][1]))

print(ans)