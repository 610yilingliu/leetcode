#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode):
        if not head:
            return False
        walked = set()
        while head.next:
            if head in walked:
                return True
            walked.add(head)
            head = head.next
        return False

# @lc code=end

