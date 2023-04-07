"""
https://www.acmicpc.net/problem/1700
1700.멀티탭 스케줄링
골드1
풀이1.76ms
"""
import sys

N, K = map(int, input().split())
nums = list(map(int, input().split()))
plugs = set()
sheep_count = 0

for index, num in enumerate(nums):
    if num in plugs:
        continue

    if len(plugs) < N:
        plugs.add(num)
        continue

    max_next_time = 0
    unplug_num = 0

    for plug in plugs:
        for i in range(index + 1, len(nums)):
            if plug == nums[i]:
                next_time = i - index
                if max_next_time < next_time:
                    max_next_time = next_time
                    unplug_num = plug
                break
        else:
            max_next_time = sys.maxsize
            unplug_num = plug

    plugs.remove(unplug_num)
    plugs.add(num)
    sheep_count += 1
print(sheep_count)



