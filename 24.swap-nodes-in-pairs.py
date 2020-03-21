#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        if head == None:
            return None
        ls = self.tolist(head, [])
        for idx in range(1, len(ls)):
            if idx % 2 == 1:
                ls[idx - 1], ls[idx] = ls[idx], ls[idx - 1]
        ln = self.tolistnode(ls)
        return ln

    def tolist(self, ln, ls):
        ls.append(ln.val)
        if ln.next is not None:
            return self.tolist(ln.next, ls)
        return ls

    def tolistnode(self, ls):
        start = None
        previous = None
        for item in ls:
            current = ListNode(item)
            if start == None:
                start = current
            if previous is not None:
                previous.next = current
            previous = current
        return start
# @lc code=end

