"""
https://www.acmicpc.net/problem/14921
14921.용액 합성하기
풀이1.96ms
"""
N = int(input())
numbers = list(map(int, input().split()))
left = 0
right = N - 1
sheep_count = numbers[0] + numbers[-1]

while left < right:
    sum = numbers[left] + numbers[right]
    sheep_count = sheep_count if abs(sheep_count) < abs(sum) else sum
    if sum < 0:
        left += 1
    elif sum > 0:
        right -= 1
    else:
        break

print(sheep_count)