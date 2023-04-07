"""
https://leetcode.com/problems/palindrome-linked-list/
234.Palindrome Linked List
Easy
리스트
풀이3.856ms
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nums = list()

        while head:
            nums.append(head.val)
            head = head.next

        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] != nums[right]:
                return False
            left += 1
            right -= 1

        return True