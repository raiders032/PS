"""
https://www.acmicpc.net/problem/1193
1193.분수찾기
브론즈2
풀이1.
"""
n = int(input())
cnt = 0

while n > 0:
    cnt += 1
    n -= cnt

if cnt % 2:
    print(f'{cnt + n}/{1 - n}')
else:
    print(f'{1 - n}/{cnt + n}')
