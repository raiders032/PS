"""
https://programmers.co.kr/learn/courses/30/lessons/42895
N으로 표현
레벨3
다이나믹 프로그래밍
풀이1
"""


def solution(N, number):
    dp = [{int(str(N) * i)} for i in range(1, 9)]

    for N_count in range(8):
        for i in range((N_count - 1) // 2 + 1):
            for left_op in dp[i]:
                for right_op in dp[N_count - i - 1]:
                    dp[N_count].add(left_op + right_op)
                    dp[N_count].add(left_op - right_op)
                    dp[N_count].add(right_op - left_op)
                    dp[N_count].add(left_op * right_op)
                    if right_op != 0:
                        dp[N_count].add(left_op // right_op)
                    if left_op != 0:
                        dp[N_count].add(right_op // left_op)

        if number in dp[N_count]:
            return N_count + 1
    else:
        return -1
