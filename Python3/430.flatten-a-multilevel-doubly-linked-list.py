#
# @lc app=leetcode id=430 lang=python3
#
# [430] Flatten a Multilevel Doubly Linked List
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return
        save_ls = []
        pointer = head
        def traveller(head):
            if head.child:
                if head.next:
                    save_ls.append(head.next)
                head.next = head.child
                head.child = None
                head.next.prev = head
                head = head.next
            elif head.next:
                head = head.next
            elif save_ls:
                newnxt = save_ls.pop()
                head.next = newnxt
                newnxt.prev = head
                head = newnxt
            else:
                return
            traveller(head)
            
        traveller(pointer)
        return head

# @lc code=end

