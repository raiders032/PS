"""
https://www.acmicpc.net/problem/17140
17140.이차원 배열과 연산
골드4
풀이1.
"""
import sys
import collections
import heapq
input = sys.stdin.readline


def operate_r():
    global board
    most_length = 0
    sorted_records = []

    for record in board:
        sorted_record = sort_record(record)
        most_length = max(most_length, len(sorted_record))
        sorted_records.append(sorted_record)

    for record in sorted_records:
        for _ in range(most_length - len(record)):
            record.append(0)

    board = sorted_records


def operate_c():
    global board
    most_length = 0
    sorted_records = []

    for y in range(len(board[0])):
        record = []
        for x in range(len(board)):
            record.append(board[x][y])
        sorted_record = sort_record(record)
        most_length = max(most_length, len(sorted_record))
        sorted_records.append(sorted_record)

    for record in sorted_records:
        for _ in range(most_length - len(record)):
            record.append(0)

    result = [[0] * len(sorted_records) for _ in range(len(sorted_records[0]))]
    for i in range(len(sorted_records)):
        for j, number in enumerate(sorted_records[i]):
            result[j][i] = number
    board = result


def sort_record(record):
    counter = collections.defaultdict(int)
    for number in record:
        if number == 0:
            continue
        counter[number] += 1

    heap = []
    for number, count in counter.items():
        heapq.heappush(heap, (count, number))

    result = []
    for count, number in heap:
        result.append(number)
        result.append(count)
    return result[:100]


r, c, k = map(int, input().split())
board = [list(map(int, input().rstrip().split())) for _ in range(3)]
sheep_count = 0

while sheep_count < 100:
    if r - 1 < len(board) and c - 1 < len(board[0]) and board[r - 1][c - 1] == k:
        break
    print('-----------------------------------')
    print(board)
    if len(board) >= len(board[0]):
        operate_r()
        print("R")
    else:
        operate_c()
        print("C")
    print(board)
    sheep_count += 1

print(sheep_count if sheep_count < 100 else -1)
