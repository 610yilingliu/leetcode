#
# @lc app=leetcode id=369 lang=python3
#
# [369] Plus One Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode):
        last_not9 = None
        cur = head
        while cur:
            if cur.val != 9:
                last_not9 = cur
            cur = cur.next
        if last_not9:
            last_not9.val += 1
            curpointer = last_not9.next
            while curpointer:
                curpointer.val = 0
                curpointer = curpointer.next
            return head
        newhead = ListNode(1)
        newhead.next = head
        pointer = newhead.next
        while pointer:
            pointer.val = 0
            pointer = pointer.next
        return newhead

        
# @lc code=end

