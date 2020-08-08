/*
 * @lc app=leetcode id=531 lang=csharp
 *
 * [531] Lonely Pixel I
 */

// @lc code=start
using System.Collections.Generic;
public class Solution {
    public int FindLonelyPixel(char[][] picture) {
        Dictionary<int, int> row_dic = new Dictionary<int, int>();
        Dictionary<int, int> col_dic = new Dictionary<int, int>();
        for(int i = 0; i < picture.Length; i ++){
            for(int j = 0; j < picture[0].Length; j++){
                if(picture[i][j] == 'B'){
                    if(col_dic.ContainsKey(i)) col_dic[i] ++;
                    else col_dic.Add(i, 1);
                    if(row_dic.ContainsKey(j)) row_dic[j] ++;
                    else row_dic.Add(j, 1);
                }
            }
        }
        int row_onlyone = 0;
        int col_onlyone = 0;
        foreach(var (key, val) in col_dic){
            if(val == 1) col_onlyone ++;
        }
        foreach(var (key, val) in row_dic){
            if(val == 1) row_onlyone ++;
        }
        return Math.Min(row_onlyone, col_onlyone);
    }
}
// @lc code=end

