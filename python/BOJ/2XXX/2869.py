"""
https://www.acmicpc.net/problem/2869
2869.달팽이는 올라가고 싶다
브론즈1
풀이1.68ms
"""
A, B, V = map(int, input().split())
print((V - A) // (A - B) + 1 + (1 if (V - A) % (A - B) > 0 else 0))
