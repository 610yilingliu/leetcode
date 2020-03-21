#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = float('inf')
        tag = 0
        for i in range(len(lists)):
            if lists[i].val < head:
                head = lists[i].val
                tag = i
        head = ListNode(head)
        lists[i] = lists[i].next

# @lc code=end

