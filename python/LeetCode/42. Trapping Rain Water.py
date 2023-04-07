"""
https://leetcode.com/problems/trapping-rain-water/
42.Trapping Rain Water
Hard
풀이1.56ms
"""
heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]


def solution(heights):
    if not heights:
        return 0

    answer = 0
    max_height = max(heights)
    left = 0
    left_max_height = 0
    right = len(heights) - 1
    right_max_height = 0

    while left < right:
        if left_max_height <= right_max_height < max_height:
            if heights[right] <= right_max_height:
                answer += right_max_height - heights[right]
            else:
                right_max_height = heights[right]
            right = right - 1 if right_max_height != max_height else right
        else:
            if heights[left] <= left_max_height:
                answer += left_max_height - heights[left]
            else:
                left_max_height = heights[left]
            left += 1

    return answer


print(solution(heights))

"""
class Solution:
    def trap(self, heights: List[int]) -> int:
        if not heights:
            return 0
        sheep_count = 0
        max_height = max(heights)
        left = 0
        left_max_height = 0
        right = len(heights) - 1
        right_max_height = 0

        while left < right:
            if left_max_height <= right_max_height < max_height:
                if heights[right] <= right_max_height:
                    sheep_count += right_max_height - heights[right]
                else:
                    right_max_height = heights[right]
                right = right - 1 if right_max_height != max_height else right
            else:
                if heights[left] <= left_max_height:
                    sheep_count += left_max_height - heights[left]
                else:
                    left_max_height = heights[left]
                left += 1

        return sheep_count
"""
