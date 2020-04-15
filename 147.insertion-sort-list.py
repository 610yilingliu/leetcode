#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head):
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        while head.next:
            if head.val <= head.next.val:
                head = head.next
            else:
                temp = head.next
                cur_sort = dummy
                head.next = head.next.next
                while cur_sort.next and cur_sort.next.val < temp.val:
                    cur_sort = cur_sort.next
                temp.next = cur_sort.next
                cur_sort.next = temp
        return dummy.next

        
# @lc code=end

