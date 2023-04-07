"""
https://www.acmicpc.net/problem/1722
1722.순열의 순서
실버1
풀이1.
"""


def next_permutation():
    i = N - 1
    j = N - 1

    while i > 0 and nums[i - 1] >= nums[i]:
        i -= 1

    if i == 0:
        return False

    while i <= j:
        if nums[i - 1] <= nums[j]:
            break
        j -= 1

    nums[i - 1], nums[j] = nums[j], nums[i - 1]
    j = N - 1

    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1

    return True


N = int(input())
nums = list(map(int, input().split()))
command = nums[0]

if command == 1:
    cnt = nums[1]
    nums = [i for i in range(1, N + 1)]
    for _ in range(cnt - 1):
        next_permutation()
    print(*nums)
else:
    origin = list(nums[1:])
    nums = [i for i in range(1, N + 1)]
    cnt = 1
    while next_permutation():
        cnt += 1
        if origin == nums:
            break
    print(cnt)