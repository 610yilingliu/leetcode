/*
 * @lc app=leetcode id=448 lang=csharp
 *
 * [448] Find All Numbers Disappeared in an Array
 */

// @lc code=start
using System.Collections.Generic;
using System;
public class Solution {
    public IList<int> FindDisappearedNumbers(int[] nums) {
        HashSet<int> s = new HashSet<int>(nums);
        List<int> ans = new List<int>();
        for(int i = 1;i < nums.Length + 1; i ++){
            if(s.Contains(i) == false){
                ans.Add(i);
            }
        }
        return ans;
    }
}
// @lc code=end

