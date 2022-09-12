"""
https://school.programmers.co.kr/learn/courses/30/lessons/64062
징검다리 건너기
풀이1.100점
"""


def solution(stones, k):
    def check(number):
        count = 0
        for stone in stones:
            if stone < number:
                count += 1
                if count == k:
                    return False
            else:
                count = 0

        return True

    low = 1
    high = 200000001

    while low + 1 < high:
        mid = (low + high) // 2
        if check(mid):
            low = mid
        else:
            high = mid

    return low


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
