/*
 * @lc app=leetcode id=504 lang=csharp
 *
 * [504] Base 7
 */

// @lc code=start
public class Solution {
    public string ConvertToBase7(int num) {
        if(num == 0) return "0";
        string ans = "";
        bool neg_tag = false;
        if(num < 0){
            neg_tag = true;
            num = -num;
        }
        while(num > 0){
            int curnum = num % 7;
            string curchar = curnum.ToString();
            ans = curchar + ans;
            num = num / 7;
        }
        if(neg_tag == true){
            ans = ans.Insert(0, "-");
        }
        return ans;
    }
}
// @lc code=end

