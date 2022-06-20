"""
https://www.acmicpc.net/problem/13305
13305.주유소
실버4
풀이1.172ms
"""
N = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

min_price = prices[0]
distance = 0
answer = 0
for i in range(1, len(prices)):
    distance += distances[i - 1]
    if prices[i] < min_price:
        answer += min_price * distance
        min_price = prices[i]
        distance = 0
if distance:
    answer += distance * min_price

print(answer)
