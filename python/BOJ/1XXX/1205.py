"""
https://www.acmicpc.net/problem/1205
1205.등수 구하기
실버5
풀이2.
"""
N, score, P = map(int, input().split())
ranks = [-1] + list(map(int, input().split()))

if N == 0:
    print(1)
    exit()

left = 1
right = N
find_index = 0

while left <= right:
    mid = (left + right) // 2
    if score <= ranks[mid]:
        left = mid + 1
        find_index = mid
    else:
        right = mid - 1

if ranks[find_index] == score:
    if find_index >= P:
        print(-1)
    else:
        while find_index and ranks[find_index - 1] == score:
            find_index -= 1
        print(find_index)
else:
    if find_index < P:
        print(find_index + 1)
    else:
        print(-1)

"""
10 1 10
10 9 8 7 6 5 4 3 2 2
"""