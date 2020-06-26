#
# @lc app=leetcode id=382 lang=python3
#
# [382] Linked List Random Node
#

# @lc code=start
# Definition for singly-linked list.
import random

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.nodesls = []
        while head:
            self.nodesls.append(head)
            head = head.next

        

    def getRandom(self):
        """
        Returns a random node's value.
        """
        if len(self.nodesls) == 1:
            return self.nodesls[0].val
        ran = random.randint(0, len(self.nodesls) - 1)
        return self.nodesls[ran].val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# @lc code=end

