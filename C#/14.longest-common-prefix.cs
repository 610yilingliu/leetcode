/*
 * @lc app=leetcode id=14 lang=csharp
 *
 * [14] Longest Common Prefix
 */

// @lc code=start
using System.Text;
public class Solution {
    public string LongestCommonPrefix(string[] strs) {
        int curpos = 0;
        int l = strs.Length;
        string res;
        if(l == 0) return "";
        StringBuilder ans = new StringBuilder();
        while(true){
            try{
                var curchar = strs[0][curpos];
                for(int i = 0;i < l; i++){
                    if(strs[i][curpos] != curchar){
                        res = ans.ToString();
                        return res;
                    };
                }
                ans.Append(curchar);
                curpos ++;
            }
            catch{break;}
        }
        res = ans.ToString();
        return res;
    }
}
// @lc code=end

