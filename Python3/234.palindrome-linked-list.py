#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        # 快慢指针法找链表的中点
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        slow = slow.next # slow指向链表的后半段
        slow = self.reverseList(slow)

        while slow:
            if head.val != slow.val:
                return False
            slow = slow.next
            head = head.next
        return True

    def reverseList(self, head):
        new_head = None
        while head:
            p = head
            head = head.next
            p.next = new_head
            new_head = p
        return new_head


# @lc code=end

def ls_to_ln(ls):
    if not ls:
        return None
    head = ListNode(ls[0])
    dummy = ListNode(0)
    dummy.next = head
    for i in range(1, len(ls)):
        head.next = ListNode(ls[i])
        head = head.next
    return dummy.next

if __name__ == '__main__':
    h = ls_to_ln([1,2,2,1])
    a = Solution()
    b = a.isPalindrome(h)
    print(b)