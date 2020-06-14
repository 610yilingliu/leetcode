#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode):
        if not head:
            return None
        walked = set()
        while head.next:
            if head in walked:
                return head
            walked.add(head)
            head = head.next
        return None
# @lc code=end

