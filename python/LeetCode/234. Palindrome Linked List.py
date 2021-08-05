"""
https://leetcode.com/problems/palindrome-linked-list/
234.Palindrome Linked List
Easy
리스트
풀이2.804ms
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        list = []

        while head:
            list.append(head.val)
            head = head.next

        for i in range(len(list) // 2):
            if list[i] != list[len(list) - i - 1]:
                return False

        return True