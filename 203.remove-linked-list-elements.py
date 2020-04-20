#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int):
        dummy = ListNode(0)
        dummy.next = head
        pointer = dummy
        while head:
            if head.val == val:
                pointer.next = head.next
            else:
                pointer = pointer.next
            head = head.next
        return dummy.next

# @lc code=end

