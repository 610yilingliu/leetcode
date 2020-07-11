/*
 * @lc app=leetcode id=561 lang=csharp
 *
 * [561] Array Partition I
 */
using System;
using System.Collections.Generic;
// @lc code=start
public class Solution {
    public int ArrayPairSum(int[] nums) { 
        Array.Sort(nums);
        int s = 0;
        int l = nums.Length;
        for(int i = 0;i < l; i += 2){
            s += nums[i];
        }
        return s;
    }
}
// @lc code=end

