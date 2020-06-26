/*
 * @lc app=leetcode id=482 lang=csharp
 *
 * [482] License Key Formatting
 */

// @lc code=start
public class Solution {
    public string LicenseKeyFormatting(string S, int K) {
        string ans = "";
        int overflow_counter = 0;
        for(int i = S.Length - 1; i > -1; i --){
            if(S[i] != '-'){
                if(overflow_counter == K){
                    ans = "-" + ans;
                    overflow_counter = 0;
                }
                overflow_counter ++;
                ans = S[i] + ans;
            }
        }
        return ans.ToUpper();
    }
}
// @lc code=end

