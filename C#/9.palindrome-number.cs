/*
 * @lc app=leetcode id=9 lang=csharp
 *
 * [9] Palindrome Number
 */

// @lc code=start
public class Solution {
    public bool IsPalindrome(int x) {
        string x_s = x.ToString();
        int l = 0;
        int r = x_s.Length - 1;
        while(l < r){
            if(x_s[l] != x_s[r]) return false;
            l ++;
            r --;
        }
        return true;
    }
}
// @lc code=end

