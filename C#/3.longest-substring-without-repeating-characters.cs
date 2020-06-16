/*
 * @lc app=leetcode id=3 lang=csharp
 *
 * [3] Longest Substring Without Repeating Characters
 */

// @lc code=start
using System.Collections;
public class Solution {
    public int LengthOfLongestSubstring(string s) {
        HashSet<object> notdup = new HashSet<object>();
        Queue anslist = new Queue();
        int maxlen = 0;
        for(int i = 0;i < s.Length;i++){
            if(notdup.Contains(s[i])){
                while(anslist.Count > 0 && notdup.Contains(s[i])){
                    var curele = anslist.Dequeue();
                    notdup.Remove(curele);
                }
            }
            notdup.Add(s[i]);
            anslist.Enqueue(s[i]);
            int curlen = anslist.Count;
            maxlen = curlen > maxlen ? curlen : maxlen;
        }
        return maxlen;
    }
}
// @lc code=end

