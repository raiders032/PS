"""
https://www.acmicpc.net/problem/2748
2748.피보나치 수 2
브론즈1
풀이1.72ms
"""
N = int(input())
fibo = [0] * (N + 1)
fibo[1] = 1

for i in range(2, N + 1):
    fibo[i] = fibo[i -1] + fibo[i - 2]

print(fibo[N])