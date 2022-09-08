"""
https://www.acmicpc.net/problem/20300
20300.서강근육맨
풀이1.80ms
"""
N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

if N % 2 != 0:
    answer = numbers[-1]
    numbers = numbers[:N - 1]
else:
    answer = numbers[0] + numbers[-1]

for i in range(len(numbers) // 2):
    answer = max(answer, numbers[i] + numbers[len(numbers) - i - 1])
print(answer)