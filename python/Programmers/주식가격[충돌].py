"""
https://programmers.co.kr/learn/courses/30/lessons/42584
주식가격
레벨2
스택
풀이1
"""

def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for index, price in enumerate(prices):
        while stack and price < stack[-1][1]:
            i, p = stack.pop()
            answer[i] = index - i
        stack.append((index, price))
    while stack:
        i, p = stack.pop()
        answer[i] = len(prices) - i - 1
    return answer

print(solution([1, 2, 3, 2, 3]))

