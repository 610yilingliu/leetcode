/*
 * @lc app=leetcode id=566 lang=csharp
 *
 * [566] Reshape the Matrix
 */

// @lc code=start
using System.Collections.Generic;
    public class Solution
    {
        public int[][] MatrixReshape(int[][] nums, int r, int c)
        {
            int[][] res = new int[r][];
            int n = nums.Length;
            int m = nums[0].Length;

            if (n * m != r * c)
            {
                return nums;
            }

            int idx = 0;

            for (int i = 0; i < r; i++)
            {
                res[i] = new int[c];
                for (int j = 0; j < c; j++)
                {
                    int oldRow = idx / m;
                    int oldCol = idx % m;

                    res[i][j] = nums[oldRow][oldCol];
                    idx++;
                }
            }

            return res;
        }
    }
// @lc code=end

