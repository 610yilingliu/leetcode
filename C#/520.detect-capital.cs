/*
 * @lc app=leetcode id=520 lang=csharp
 *
 * [520] Detect Capital
 */
using System;
// @lc code=start
public class Solution {
    public bool DetectCapitalUse(string word) {
        if(word == null) return false;
        int ucount = 0;
        bool l = false;
        for(int i = 0; i < word.Length; i ++){
            if(i > 0 && l){
                if(Char.IsUpper(word[i])) return false;
            }
            if(ucount > 1 && Char.IsLower(word[i])) return false;
            if(Char.IsUpper(word[i])){
                ucount ++;
            }
            else{
                l = true;
            }
        }
        return true;
    }
}
// @lc code=end

