/*
 * @lc app=leetcode id=356 lang=csharp
 *
 * [356] Line Reflection
 */

// @lc code=start
using System.Collections.Generic;
public class Solution {
    public bool IsReflected(int[][] points) {
        HashSet<(int, int)> ps = new HashSet<(int, int)>();
        float add_up = 0;
        foreach(int[] point in points){
            if(ps.Contains((point[0], point[1])) is false){
                add_up += point[0];
            }
            ps.Add((point[0], point[1]));
        }
        float added = (float)add_up;
        float mid = added/(ps.Count);
        foreach(int[] point in points){
            int ref_x = (int)(mid - (point[0] - mid));
            if(ps.Contains((ref_x, point[1])) is false) return false;
        }
        return true;
    }
}
// @lc code=end

