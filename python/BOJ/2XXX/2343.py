'''
2343번 기타 레슨 실버1
이분탐색
'''
N, M = map(int, input().split())
arr = list(map(int, input().split()))
left = 1
right = sum(arr)
res = 0
min_size = max(arr)


def getCnt(c):
    cnt = 1
    sum = 0
    for x in arr:
        if sum + x <= c:
            sum += x
        else:
            cnt += 1
            sum = x
    return cnt


while left <= right:
    mid = (right + left) // 2
    cnt = getCnt(mid)
    if cnt > M or mid < min_size:
        left = mid + 1
    else:
        res = mid
        right = mid - 1
print(res)
