"""
https://www.acmicpc.net/problem/2212
2212.센서
골드5
풀이1.76ms
"""
N = int(input())
K = int(input())
sensors = list(map(int, input().split()))
sensors.sort()
diff = [sensors[i + 1] - sensors[i] for i in range(N - 1)]
diff.sort(reverse=True)
print(sum(diff[K - 1:]))