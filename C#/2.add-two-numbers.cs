/*
 * @lc app=leetcode id=2 lang=csharp
 *
 * [2] Add Two Numbers
 */

// @lc code=start
// using System.Collections.Generic;
//  public class ListNode {
//      public int val;
//      public ListNode next;
//      public ListNode(int val=0, ListNode next=null) {
//          this.val = val;
//          this.next = next;
//      }
//  }

public class Solution
    {
        public ListNode AddTwoNumbers(ListNode l1, ListNode l2){
            ListNode head = new ListNode();
            var pointer = head;
            int curval = 0;
            while(l1 != null || l2 != null){
                curval = (l1 == null ? 0 : l1.val) + (l2 == null ? 0 : l2.val) + curval;
                pointer.next = new ListNode(curval % 10);
                pointer = pointer.next;
                // overflow decimal, like 12, we keep 1 for the next loop
                curval = curval / 10;
                // if next l1/l2 is not null, go to the next node
                l1 = l1?.next;
                l2 = l2?.next;
            }
            // if there is overflow left, add a node
            if(curval != 0){
                pointer.next = new ListNode(curval);
            }
            return head.next;
        }
    }
// @lc code=end

