/*
 * @lc app=leetcode id=506 lang=csharp
 *
 * [506] Relative Ranks
 */

// @lc code=start
// using System;
// using System.Collections.Generic;
// public class heapq{
//     List<int> h = new List<int>();
//     int lastidx = -1;
//     public void heappush(int num){
//         h.Add(num);
//         lastidx ++;
//         int parent = (lastidx - 1) >> 1;
//         int curidx = lastidx;
//         while(num > h[parent]){
//         // switch if parent is smaller
//             h[curidx] = h[parent];
//             h[parent] = num;
//             curidx = parent;
//             parent = (parent - 1) >> 1;
//         }
//     }
//     public heappop(){
//         int to_return = h[0];
//         h[0] = h[lastidx];
//         // O(1) according to MSDN https://docs.microsoft.com/en-us/dotnet/api/system.collections.generic.list-1.removeat?view=netcore-3.1
//         h.RemoveAt(lastidx);
//         lastidx --;
//         if(lastidx < 1){
//             return to_return;
//         }
//         if(lastidx == 1){
//             h.Sort((x, y) => -x.CompareTo(y));
//             return to_return;
//         }
//         // if len(list) > 2
//         shift_down(0);
//         return to_return;
//     }
//     public void shift_down(int parent){
//         int left_child = 2 * parent + 1;
//         int right_child = 2 * parent + 2;
//         int curlargest = h[parent];
//         if(left_child < lastidx && right_child <= lastidx){
//             if(h[left_child] > curlargest){
//                 h[parent] = h[left_child];
//                 h[left_child] = curlargest;
//                 shift_down(left_child);
//             }
//             else if(h[right_child] > curlargest){
//                 h[parent] = h[right_child];
//                 h[right_child] = curlargest;
//                 shift_down(right_child);
//             }
//         }
//         else if(left_child == lastidx){
//             if(h[left_child] > curlargest){
//                 h[parent] = h[left_child];
//                 h[left_child] = curlargest;
//             }
//         }
//     }
// }
    public class Solution
    {
        public string[] FindRelativeRanks(int[] nums)
        {
            (int score, int idx)[] data = new (int score, int idx)[nums.Length];
            for (int i = 0; i < nums.Length; i++)
            {
                data[i] = (nums[i], i);
            }

            Array.Sort(data, (d1, d2) => d2.score.CompareTo(d1.score));
            string[] res = new string[nums.Length];
            for (int i = 0; i < nums.Length; i++)
            {
                if (i == 0)
                {
                    res[data[i].idx] = "Gold Medal";
                    continue;
                }

                if (i == 1)
                {
                    res[data[i].idx] = "Silver Medal";
                    continue;
                }

                if (i == 2)
                {
                    res[data[i].idx] = "Bronze Medal";
                    continue;
                }

                res[data[i].idx] = (i + 1).ToString();
            }

            return res;
        }
    }
// @lc code=end

