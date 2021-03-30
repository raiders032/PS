"""
https://programmers.co.kr/learn/courses/30/lessons/68644?language=python3
두 개 뽑아서 더하기
레벨1
풀이1
"""
def solution(numbers):
    sum_set = set()
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            sum_set.add(numbers[i] + numbers[j])
    return sorted(list(sum_set))


print(solution([2,1,3,4,1]))