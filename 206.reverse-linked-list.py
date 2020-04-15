#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        tail = None
        while head:
            temp = head.next
            head.next = tail
            tail = head
            head = temp
        return tail
# @lc code=end

