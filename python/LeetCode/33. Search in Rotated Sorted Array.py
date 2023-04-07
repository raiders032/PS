from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bi_search(left, right):
            if right < left:
                return -1
            mid = (right + left) // 2
            if nums[mid] < target:
                return bi_search(mid + 1, right)
            elif target < nums[mid]:
                return bi_search(left, mid - 1)
            else:
                return mid

        pivot = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                pivot = i
                break
        nums = nums[pivot + 1:] + nums[:pivot + 1]
        result = bi_search(0, len(nums) - 1)

        return result + pivot + 1


print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))
