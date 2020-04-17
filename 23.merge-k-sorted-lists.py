#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
import heapq

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        dummy = ListNode(0)
        pointer = dummy
        heap = []
        heapq.heapify(heap)
        for idx, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, idx))
        while heap:
            curval, curidx = heapq.heappop(heap)
            curhead = lists[curidx]
            curnxt = curhead.next
            pointer.next = curhead
            curhead.next = None
            pointer = curhead
            curhead = curnxt
            if curhead is not None:
                lists[curidx] = curhead
                heapq.heappush(heap, (curnxt.val, curidx))
        return dummy.next


# @lc code=end


