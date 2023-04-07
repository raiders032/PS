"""
https://programmers.co.kr/learn/courses/30/lessons/42626
더 맵게
레벨2
풀이1
"""
import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville) >= 2 and scoville[0] < K:
        min_scoville1 = heapq.heappop(scoville)
        min_scoville2 = heapq.heappop(scoville)
        heapq.heappush(scoville, min_scoville1 + 2 * min_scoville2)
        answer += 1

    if scoville and scoville[0] < K:
        return -1

    return answer
