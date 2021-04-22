class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0
        max_height = 0
        max_height_index = 0
        max_left_height = 0
        max_right_height = 0

        for index, value in enumerate(height):
            if value > max_height:
                max_height = value
                max_height_index = index

        left = 0
        right = len(height) - 1

        while left < max_height_index:
            if height[left] < max_left_height:
                answer += max_left_height - height[left]
            else:
                max_left_height = height[left]
            left += 1

        while max_height_index < right:
            if height[right] < max_right_height:
                answer += max_right_height - height[right]
            else:
                max_right_height = height[right]
            right -= 1

        return answer