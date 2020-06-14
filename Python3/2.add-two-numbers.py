#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ln = ListNode(0)
        current = ln
        tpsum = 0
        while l1 or l2 or tpsum:
            if l1:
                tpsum += l1.val
                l1 = l1.next
            if l2:
                tpsum += l2.val
                l2 = l2.next
            current.next = ListNode(tpsum%10)
            current = current.next
            tpsum = tpsum//10
        return ln.next

        
# @lc code=end

