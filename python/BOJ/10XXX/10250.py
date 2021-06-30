"""
https://www.acmicpc.net/problem/10250
10250.ACM 호텔
브론즈3
수학
풀이1.76ms
"""
test_case = int(input())
for i in range(test_case):
    H, W, N = map(int, input().split())
    YY = N % H if N % H != 0 else H
    XX = (N - 1) // H + 1
    if len(str(XX)) == 1:
        print(f'{YY}0{XX}')
    else:
        print(f'{YY}{XX}')
