#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        node_d = dict()
        dummy = Node(0, None, None)
        node_d[head] = dummy
        nh, pointer = dummy, head
        while pointer:
            node = Node(pointer.val, pointer.next, None)
            node_d[pointer] = node
            nh.next = node
            nh, pointer = nh.next, pointer.next
        pointer = head
        while pointer:
            if pointer.random:
                node_d[pointer].random = node_d[pointer.random]
            pointer = pointer.next
        return dummy.next
# @lc code=end

