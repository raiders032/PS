"""
https://programmers.co.kr/learn/courses/30/lessons/42746
가장 큰 수
정렬
레벨2
풀이1
"""


def solution(numbers):
    numbers.sort(key=lambda x: int((str(x) * 4)[:4]), reverse=True)
    if numbers[0] == 0:
        return "0"
    return ''.join(map(str, numbers))


print(solution([3, 30, 34, 5, 9]))