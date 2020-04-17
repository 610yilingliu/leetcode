#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
import collections
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        tplist = collections.deque()
        counter = 0
        while head:
            # if the queue fulled, pop everyting inside it, let the current node connect to them
            if counter == k:
                while counter > 0:
                    cur.next = tplist.pop()
                    cur = cur.next
                    counter -= 1
            # else put things to queue
            else:
                tplist.append(head)
                head = head.next
                counter += 1
        # connect reversely if the rest queue is full
        if len(tplist) == k:
            while tplist:
                cur.next = tplist.pop()
                cur = cur.next
            cur.next = None
        # else connect without reverse
        elif len(tplist) > 0:
            while tplist:
                cur.next = tplist.popleft()
                cur = cur.next
        return dummy.next

if __name__ == '__main__':
    S = Solution()
    l1 = ListNode(1)
    l2 = ListNode(2)
    # l3 = ListNode(3)
    # l4 = ListNode(4)
    # l5 = ListNode(5)
    head = l1
    l1.next = l2
    l2.next = None
    # l3.next = l4
    # l4.next = l5
    # l5.next = None
    a = S.reverseKGroup(head, 2)  
    print(a)
    
        


# @lc code=end

