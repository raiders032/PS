"""
https://www.acmicpc.net/problem/4153
4153.직각삼각형
브론즈3
풀이1.68ms
"""
while True:
    arr = list(map(int, input().split()))
    if arr == [0, 0, 0]:
        break
    arr.sort()
    if arr[0] ** 2 + arr[1] ** 2 == arr[2] ** 2:
        print("right")
    else:
        print("wrong")
