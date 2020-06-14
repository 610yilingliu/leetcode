#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        root = ListNode(0)
        p = root
        q = head

        for _ in range(m-1):
            p.next = q
            q = q.next
            p = p.next

        end = q
        start = None
        next = None

        for _ in range(m, n + 1):
            next = q.next
            q.next = start
            start = q
            q = next
        
        p.next = start
        end.next = next
        return root.next

if __name__ == '__main__':
    S = Solution()
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    head = l1
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l5.next = None
    a = S.reverseBetween(head,2,4)    
    print(a)
    


# @lc code=end

