/*
 * @lc app=leetcode id=557 lang=csharp
 *
 * [557] Reverse Words in a String III
 */
// @lc code=start
public class Solution {
    public string ReverseWords(string s) {
        var strings = s.Split(' ');
        var sb = new StringBuilder();
        foreach (string str in strings) {
            int l = str.Length;
            for(int i = l - 1; i > -1; i--) {
                sb.Append(str[i]);
            }
            sb.Append(' ');
        }
        return sb.ToString().TrimEnd();
    }
}
// @lc code=end

