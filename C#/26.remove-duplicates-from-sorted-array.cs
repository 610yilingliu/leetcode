/*
 * @lc app=leetcode id=26 lang=csharp
 *
 * [26] Remove Duplicates from Sorted Array
 */

// @lc code=start
public class Solution {
    public int RemoveDuplicates(int[] nums) {
        if(nums.Length == 0) return 0;
        int cur = nums[0];
        int cnt = 1;
        for(int i = 0; i < nums.Length; i ++){
            if(nums[i] != cur){
                cur = nums[i];
                nums[cnt] = nums[i];
                cnt ++;
            }
        }
        return cnt;
    }
}
// @lc code=end

