/*
 * @lc app=leetcode id=20 lang=csharp
 *
 * [20] Valid Parentheses
 */

// @lc code=start
using System.Collections.Generic;
public class Solution {
    public bool IsValid(string s) {
        Dictionary<char, char> parenthses = new Dictionary<char, char>();
        parenthses[')'] = '(';
        parenthses[']'] = '[';
        parenthses['}'] = '{';
        Stack<char> st = new Stack<char>();
        var p = s.ToCharArray();
        foreach(var item in p){
            if(st.Count > 0 && parenthses.ContainsKey(item) && st.Peek() == parenthses[item]){
                st.Pop();
            }
            else{
                st.Push(item);
            }
        }
        return st.Count == 0;
    }
}
// @lc code=end

