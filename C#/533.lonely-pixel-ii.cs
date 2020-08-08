/*
 * @lc app=leetcode id=533 lang=csharp
 *
 * [533] Lonely Pixel II
 *
 * https://leetcode.com/problems/lonely-pixel-ii/description/
 *
 * algorithms
 * Medium (47.40%)
 * Likes:    50
 * Dislikes: 552
 * Total Accepted:    10.4K
 * Total Submissions: 21.8K
 * Testcase Example:  '[["W","B","W","B","B","W"],["W","B","W","B","B","W"],["W","B","W","B","B","W"],["W","W","B","W","B","W"]]\n' +
  '3'
 *
 * Given a picture consisting of black and white pixels, and a positive integer
 * N, find the number of black pixels located at some specific row R and column
 * C that align with all the following rules:
 * 
 * 
 * ⁠Row R and column C both contain exactly N black pixels.
 * ⁠For all rows that have a black pixel at column C, they should be exactly
 * the same as row R
 * 
 * 
 * The picture is represented by a 2D char array consisting of 'B' and 'W',
 * which means black and white pixels respectively. 
 * 
 * Example:
 * 
 * Input:                                            
 * [['W', 'B', 'W', 'B', 'B', 'W'],    
 * ⁠['W', 'B', 'W', 'B', 'B', 'W'],    
 * ⁠['W', 'B', 'W', 'B', 'B', 'W'],    
 * ⁠['W', 'W', 'B', 'W', 'B', 'W']] 
 * 
 * N = 3
 * Output: 6
 * Explanation: All the bold 'B' are the black pixels we need (all 'B's at
 * column 1 and 3).
 * ⁠       0    1    2    3    4    5         column
 * index                                            
 * 0    [['W', 'B', 'W', 'B', 'B', 'W'],    
 * 1     ['W', 'B', 'W', 'B', 'B', 'W'],    
 * 2     ['W', 'B', 'W', 'B', 'B', 'W'],    
 * 3     ['W', 'W', 'B', 'W', 'B', 'W']]    
 * row index
 * 
 * Take 'B' at row R = 0 and column C = 1 as an example:
 * Rule 1, row R = 0 and column C = 1 both have exactly N = 3 black pixels. 
 * Rule 2, the rows have black pixel at column C = 1 are row 0, row 1 and row
 * 2. They are exactly the same as row R = 0.
 * 
 * 
 * 
 * 
 * Note:
 * 
 * The range of width and height of the input 2D array is [1,200].
 * 
 * 
 */
// @lc code=start
    public class Solution
    {
        private class Row : IEquatable<Row>
        {
            private readonly ulong[] _raw;

            public Row()
            {
                _raw = new ulong[4];
            }

            public void Set(int bitNumber)
            {
                int _rawIdx = bitNumber / 64;
                int bitMod = bitNumber % 64;
                _raw[_rawIdx] |= (1UL << bitMod);
            }

            public override bool Equals(object obj) => Equals((Row) obj);
            public bool Equals(Row other) => _raw.SequenceEqual(other._raw);
            public override int GetHashCode() => (_raw[0], _raw[1], _raw[2], _raw[3]).GetHashCode();
        }

        public int FindBlackPixel(char[][] picture, int target)
        {
            int n = picture.Length;
            int m = picture[0].Length;

            int[] rowsBCount = new int[n];
            int[] colsBCount = new int[m];
            

            IDictionary<Row, int> isoRowsMap = new Dictionary<Row, int>();
            Row[] rowForms = new Row[n];

            for (int i = 0; i < n; i++)
            {
                Row r = new Row();

                for (int j = 0; j < m; j++)
                {
                    if (picture[i][j] == 'B')
                    {
                        r.Set(j);
                        rowsBCount[i]++;
                        colsBCount[j]++;
                    }
                }

                if (!isoRowsMap.ContainsKey(r))
                {
                    isoRowsMap[r] = 0;
                }

                isoRowsMap[r]++;
                rowForms[i] = r;
            }

            int res = 0;

            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < m; j++)
                {
                    if (picture[i][j] == 'B' && rowsBCount[i] == target && colsBCount[j] == target && isoRowsMap[rowForms[i]] == target)
                    {
                        res++;
                    }
                }
            }

            return res;
        }
    }
// @lc code=end

