/*
 * @lc app=leetcode id=96 lang=csharp
 *
 * [96] Unique Binary Search Trees
 */
using System.Collections.Generic;
// @lc code=start
public class Solution {
    public int NumTrees(int n) {
        List<int> dp = new List<int>();
        dp.Add(1);
        dp.Add(1);
        for(int curend = 1;curend < n; curend++){
            int Cnum = 0;
            for(int i = 0; i <= curend; i++){
                Cnum += dp[i] * dp[curend - i];
            }
            dp.Add(Cnum);
        }
        return dp[n];
    }
}
// @lc code=end

