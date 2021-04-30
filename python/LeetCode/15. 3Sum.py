"""
https://leetcode.com/problems/3sum/submissions/
15. 3Sum
투포인터
Medium
풀이2.848ms
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                total_sum = nums[i] + nums[left] + nums[right]

                if total_sum < 0:
                    left += 1

                elif total_sum > 0:
                    right -= 1

                else:
                    answer.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
        return answer