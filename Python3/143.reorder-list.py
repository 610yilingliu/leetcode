#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import collections

class Solution:
    def reorderList(self, head: ListNode):
        if not head:
            return None
        ls = collections.deque()
        while head:
            ls.append(head)
            head = head.next
        counter = 0
        cur = None
        while len(ls) > 0:
            if ls and counter & 1 == 0:
                if not cur:
                    cur = ls.popleft()
                if ls:
                    nxt = ls.pop()
                    cur.next = nxt
                    cur = nxt
            if ls and counter & 1:
                nxt = ls.popleft()
                cur.next = nxt
                cur = nxt
            counter += 1
        cur.next = None

            


        
# @lc code=end

