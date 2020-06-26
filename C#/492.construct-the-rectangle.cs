/*
 * @lc app=leetcode id=492 lang=csharp
 *
 * [492] Construct the Rectangle
 */

// @lc code=start
using System;
public class Solution {
    public int[] ConstructRectangle(int area) {
        if(area == 0){
            return new int[]{0, 0};
        }
        int sq = (int)Math.Sqrt(area);
        while(area % sq != 0){
           sq --;
        }
        int another = area/sq;
        int h = Math.Min(sq, another);
        int l = Math.Max(sq, another);
        return new int[]{l, h};
    }
}
// @lc code=end

