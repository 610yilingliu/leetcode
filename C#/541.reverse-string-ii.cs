/*
 * @lc app=leetcode id=541 lang=csharp
 *
 * [541] Reverse String II
 */

// @lc code=start
using System;
public class Solution {
    public string ReverseStr(string s, int k) {
        int l = s.Length;
        string ans = "";
        for(int i = 0; i < l; i += 2* k){
            int rev_end = Math.Min(i + k, l);
            for(int j = rev_end - 1; j > i - 1; j --){
                ans += s[j];
            }
            if(i + k < l){
                int end = Math.Min(i + 2 * k, l);
                for(int j = rev_end; j < end; j ++){
                    ans += s[j];
                }
            }
        }
        return ans;
    }
}
// @lc code=end

