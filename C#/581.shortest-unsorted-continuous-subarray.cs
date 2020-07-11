/*
 * @lc app=leetcode id=581 lang=csharp
 *
 * [581] Shortest Unsorted Continuous Subarray
 */
using System;
// @lc code=start
public class Solution {
    public int FindUnsortedSubarray(int[] nums) {
        if(nums is null) return 0;
        int[] sorted_nums = new int[nums.Length];
        Array.Copy(nums, sorted_nums, nums.Length);
        Array.Sort(sorted_nums);
        int minidx = -1;
        int maxidx = -1;
        for(int i = 0; i < sorted_nums.Length; i ++){
            if(sorted_nums[i] != nums[i]){
                minidx = i;
                break;
            }
        }
        for(int i = sorted_nums.Length - 1; i > -1; i --){
            if(sorted_nums[i] != nums[i]){
                maxidx = i;
                break;
            }
        }
        if(minidx > -1) return maxidx - minidx + 1;
        return 0;

    }
}
// @lc code=end

