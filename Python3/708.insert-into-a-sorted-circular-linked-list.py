#
# @lc app=leetcode id=708 lang=python3
#
# [708] Insert into a Sorted Circular Linked List
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        cur = None
        next_ = None
        min_head = None
        
        if not head:
            head = Node(insertVal)
            head.next = head
            return head
              
        cur = head
        next_ = head.next
        while cur.val <= next_.val:
            cur = cur.next
            next_ = next_.next
            
            if cur == head:
                break
        min_head = next_
                
        
        while next_.val < insertVal:
            cur = next_
            next_ = next_.next
            
            if next_ == min_head:
                break

        cur.next = Node(insertVal)
        cur = cur.next
        cur.next = next_
        
        return head

# @lc code=end

