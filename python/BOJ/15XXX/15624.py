"""
https://www.acmicpc.net/problem/15624
15624.피보나치 수 7
실버4
풀이1.412ms
"""
n = int(input())
fib = [0] * (n + 2)
fib[1] = 1

for i in range(2, n + 1):
    fib[i] = (fib[i - 1] + fib[i - 2]) % 1000000007

print(fib[n])