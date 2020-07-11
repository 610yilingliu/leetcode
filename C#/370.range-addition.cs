/*
 * @lc app=leetcode id=370 lang=csharp
 *
 * [370] Range Addition
 */

// @lc code=start
public class Solution {
    public int[] GetModifiedArray(int length, int[][] updates) {
        int[] ls = new int[length + 1];
        foreach(int[] update in updates){
            int start = update[0];
            int end = update[1] + 1;
            int step = update[2];
            ls[start] += step;
            ls[end] -= step;
            }
        for(int i = 1;i < length; i ++){
            ls[i] += ls[i - 1];
        }
        return ls[0..length];
    }
}
// @lc code=end

