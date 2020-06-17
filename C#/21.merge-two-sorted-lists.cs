/*
 * @lc app=leetcode id=21 lang=csharp
 *
 * [21] Merge Two Sorted Lists
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode MergeTwoLists(ListNode l1, ListNode l2) {
        if(l1 == null || l2 == null){
            return l1 == null ? l2 : l1;
        }
        var head = new ListNode(Smaller(ref l1, ref l2));
        var cur = head;
        while(l1 != null || l2 != null){
            if(l1 == null){
                cur.next = l2;
                break;
            }
            else if(l2 == null){
                cur.next = l1;
                break;
            }
            cur.next = new ListNode(Smaller(ref l1, ref l2));
            cur = cur.next;
        }
        return head;
    }
    public int Smaller(ref ListNode l1, ref ListNode l2){
        int val;
        if(l1 != null && l2 != null){
            if(l1.val <= l2.val){
                val = l1.val;
                l1 = l1.next;
            }
            else{
                val = l2.val;
                l2 = l2.next;
            }
        }
        else if(l1 == null){
            val = l2.val;
            l2 = l2.next;
        }
        else{
            val = l1.val;
            l1 = l1.next;
        }
        return val;
    }
}
// @lc code=end

