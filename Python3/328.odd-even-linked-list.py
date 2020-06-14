#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head):
        if not head:
            return None
        counter = 0
        odd = ListNode(0)
        even = ListNode(0)
        oddstart = odd
        evenstart = even
        while head:
            counter += 1
            if counter & 1:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            head = head.next
        even.next = None
        odd.next = evenstart.next
        return oddstart.next


# @lc code=end

