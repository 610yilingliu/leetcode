/*
 * @lc app=leetcode id=434 lang=csharp
 *
 * [434] Number of Segments in a String
 */

// @lc code=start
public class Solution {
    public int CountSegments(string s) {
        int cnt = 0;
        bool haschar = false;
        for(int i = 0; i < s.Length; i ++){
            if(haschar == false && s[i]!= ' '){
                cnt += 1;
                haschar = true;
            }
            else if(haschar == true && i > 0 && s[i - 1]== ' ' && s[i] != ' '){
                cnt += 1;
            }
        }
        return cnt;
    }
}
// @lc code=end

