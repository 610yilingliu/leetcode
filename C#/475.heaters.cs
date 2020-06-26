/*
 * @lc app=leetcode id=475 lang=csharp
 *
 * [475] Heaters
 */

// @lc code=start
using System;
using System.Collections.Generic;public class Solution {
    public int findav(int a, int b)
        {
            if (a < b)
            {
                return b - a;
            }
            return a - b;
        }
        public int FindRadius(int[] houses, int[] heaters)
        {
            if (houses.Length == 0)
            {
                return 0;
            }
            if (heaters.Length == 0)
            {
                return 2147483647;
            }
            Array.Sort(houses);
            Array.Sort(heaters);
            int longest = 0;
            int h = 0;
            for (int i = 0; i < houses.Length; i++)
            {
                int distance;
                if (h != heaters.Length - 1 && houses[i] >= heaters[h + 1])
                {
                    while (h != heaters.Length - 1 && houses[i] >= heaters[h + 1])
                    {
                        h += 1;
                    }
                }
                if (h == heaters.Length - 1)
                {
                    distance = findav(heaters[h], houses[i]);
                }
                else
                {
                    distance = Math.Min(findav(heaters[h], houses[i]), findav(heaters[h + 1], houses[i]));
                }
                longest = Math.Max(distance, longest);
            }
            return longest;
        }
}
// @lc code=end

