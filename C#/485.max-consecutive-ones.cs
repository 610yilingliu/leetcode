/*
 * @lc app=leetcode id=485 lang=csharp
 *
 * [485] Max Consecutive Ones
 */
using System;
// @lc code=start
public class Solution {
    public int FindMaxConsecutiveOnes(int[] nums) {
        int counter = 0;
        int mxlen = 0;
        foreach(int num in nums){
            if(num == 1){
                counter ++;
            }
            else{
                mxlen = Math.Max(counter, mxlen);
                counter = 0;
            }
        }
        mxlen = Math.Max(counter, mxlen);
        return mxlen;
    }
}
// @lc code=end

