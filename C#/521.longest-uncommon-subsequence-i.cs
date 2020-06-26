/*
 * @lc app=leetcode id=521 lang=csharp
 *
 * [521] Longest Uncommon Subsequence I 
 */
using System;
// @lc code=start
public class Solution {
    public int FindLUSlength(string a, string b) {
        int mx = Math.Max(a.Length, b.Length);
        return a != b ? mx : -1;
    }
}
// @lc code=end

