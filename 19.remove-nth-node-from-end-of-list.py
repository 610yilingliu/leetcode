#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# def tolistnode(ls):
#     first = None
#     previous = None
#     for item in ls:
#         current = ListNode(item)
#         if first is None:
#             first = current
#         if previous is not None:
#             previous.next = current
#         previous = current
#     return first


# class Solution:
#     def removeNthFromEnd(self, head, n):
#         if head.next == None:
#             return None
#         idx = []
#         indexed = self.helper(head, idx)
#         indexed.pop(-n)
#         if len(indexed) == 1:
#             return ListNode(indexed[0])
#         res = tolistnode(indexed)
#         return res
    
#     def helper(self, ln, ls):
#         ls.append(ln.val)
#         if ln.next:
#             return self.helper(ln.next, ls)
#         return ls


class Solution:
    def removeNthFromEnd(self, head, n):
        slow = head
        fast = head
        for _ in range(n):
            fast = fast.next
        if fast is None:
            return head.next
        # if fast pointer does not reach to the end
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head

# @lc code=end

