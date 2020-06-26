/*
 * @lc app=leetcode id=453 lang=csharp
 *
 * [453] Minimum Moves to Equal Array Elements
 */

// @lc code=start
using System.Linq;
using System;
public class Solution {
    public int MinMoves(int[] nums) {
        // cannot use nums.Min() directly in Select, every time it will try to get the minimun number of list, will cause tle
        int min = nums.Min();
        return nums.Select(x => x - min).Sum();
    }
}
// @lc code=end

