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
        public ListNode AddTwoNumbers(ListNode l1, ListNode l2)
        {
            ListNode response;

            var sum = l1.val + l2.val;

            if (sum > 9)
            {
                response = new ListNode(sum % 10);
                SumRecur(l1.next, l2.next, response, 1);
            }
            else
            {
                response = new ListNode(sum);
                SumRecur(l1.next, l2.next, response, 0);
            }

            return response;
        }

        public void SumRecur(ListNode l1, ListNode l2, ListNode response, int cof)
        {
            if (l1 != null || l2 != null || cof > 0)
            {
                var sum = (l1 == null ? 0 : l1.val) + (l2 == null ? 0 : l2.val) + cof;

                if (sum > 9)
                {
                    sum = sum % 10;
                    response.next = new ListNode(sum);
                    SumRecur(l1?.next, l2?.next, response.next, 1);
                }
                else
                {
                    response.next = new ListNode(sum);
                    SumRecur(l1?.next, l2?.next, response.next, 0);
                }
            }
        }
    }
// @lc code=end

