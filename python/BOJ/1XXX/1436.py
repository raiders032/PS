"""
https://www.acmicpc.net/problem/1436
1436.영화감독 숌
실버5
풀이1.988ms
"""
count = 0
N = int(input())
num = 666
while True:
    if '666' in str(num):
        count += 1
    if count == N:
        break
    num += 1
print(num)