"""
https://www.acmicpc.net/problem/1082
1082.방 번호
골드3
풀이1.84ms
"""
N = int(input())
prices = list(map(int, input().split()))
money = int(input())
most_left_number = 0
remainder_number = 0
room_number = []

min_price = 51
for i in range(1, N):
    if prices[i] < min_price:
        min_price = prices[i]
        most_left_number = i

money -= prices[most_left_number]
room_number.append(most_left_number)

if money < 0:
    print(0)
    exit()

min_price = 51
for i in range(N):
    if prices[i] < min_price:
        min_price = prices[i]
        remainder_number = i

quantity = money // prices[remainder_number]
money -= prices[remainder_number] * quantity
for _ in range(quantity):
    room_number.append(remainder_number)

for index, number in enumerate(room_number):
    max_number = 0
    for candidate in range(number + 1, N):
        if prices[candidate] <= money + prices[number]:
            max_number = candidate

    if max_number:
        room_number[index] = max_number
        money += prices[number] - prices[max_number]

print(''.join(map(str, room_number)))