/*
 * @lc app=leetcode id=441 lang=csharp
 *
 * [441] Arranging Coins
 */

// @lc code=start

public class Solution {
    public int ArrangeCoins(int n) {
     
            int res = 0;
            for (int i = 1; i < 9804289383; i++)
            {
                if (n - i >= 0) {
                    n = n - i;
                    res++;
                }
                else
                {
                    return res;
                }
            }
            return res-1;
    }
}
// @lc code=end

