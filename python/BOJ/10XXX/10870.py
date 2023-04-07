"""
https://www.acmicpc.net/problem/10870
10870.피보나치 수 5
브론즈2
풀이1.68ms
"""
N = int(input())
fibo = [0] * (N + 2)
fibo[1] = 1
for i in range(2, N + 1):
    fibo[i] = fibo[i - 1] + fibo[i - 2]

print(fibo[N])