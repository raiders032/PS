"""
234. Palindrome Linked List
덱 변환 풀이
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q = deque()
        if not head:
            return True

        while head is not None:
            q.append(head.val)
            head = head.next

        while len(q)>1:
            if q.popleft() != q.pop():
                return False
        return True
