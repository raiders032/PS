"""
234. Palindrome Linked List
리스트 변환 풀이
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q:list = []
        if not head:
            return True

        while head is not None:
            q.append(head.val)
            head = head.next

        while len(q)>1:
            if q.pop(0) != q.pop():
                return False
        return True
