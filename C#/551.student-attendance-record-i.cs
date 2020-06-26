/*
 * @lc app=leetcode id=551 lang=csharp
 *
 * [551] Student Attendance Record I
 */
using System.Collections.Generic;
// @lc code=start
    public class Solution
    {
        public bool CheckRecord(string s)
        {
            int firstA = s.IndexOf("A");
            int lastA = s.LastIndexOf("A");

            if (firstA != lastA)
            {
                return false;
            }

            if (s.IndexOf("LLL") >= 0)
            {
                return false;
            }

            return true;
        }
    }
// @lc code=end

