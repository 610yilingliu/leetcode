#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k):
        if not head:
            return None
        if k == 0:
            return head
        ls = []
        while head:
            ls.append(head)
            head = head.next
        k = k % len(ls)
        part1 = ls[:len(ls) - k]
        part2 = ls[len(ls) - k:]
        dummy = ListNode(0)
        if part2:
            curhead = part2[0]
            dummy.next = curhead
            pointer = dummy
            while curhead:
                curhead = curhead.next
                pointer = pointer.next
            pointer.next = part1[0]
        else:
            dummy.next = part1[0]
            pointer = dummy
        for _ in range(len(part1)):
            pointer = pointer.next
        pointer.next = None
        return dummy.next

# @lc code=end

