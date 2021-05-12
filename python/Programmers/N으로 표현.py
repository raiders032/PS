"""
https://programmers.co.kr/learn/courses/30/lessons/42895
N으로 표현
레벨3
다이나믹 프로그래밍
풀이2
"""
import heapq

def solution(numbers):
    answer = ''
    heap = []

    for number in numbers:
        priority = int((str(number) * 4)[:4])
        heapq.heappush(heap, (-priority, number))

    while heap:
        answer += heapq.heappop(heap)[1]

    return answer


print(solution(['3', '308']))