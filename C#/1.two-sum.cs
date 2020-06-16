/*
 * @lc app=leetcode id=1 lang=csharp
 *
 * [1] Two Sum
 */
using System.Collections.Generic;
// @lc code=start
public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        int len = nums.Length;
        Dictionary<int, int> walked = new Dictionary<int, int>();
        for(int i = 0; i < len; i ++){
            var rest = target - nums[i];
            if(walked.ContainsKey(rest))
                return new int[]{walked[rest], i};
            else
                if(!walked.ContainsKey(nums[i]))
                    walked.Add(nums[i], i);
        }
        return new int[0];
    }
    static void Main(){
        var a = new Solution();
        int[] b = {1, 2, 3, 4, 5};
        int s = 7; 
        var ans = a.TwoSum(b, s);
        // foreach(int element in ans){
        //     System.Console.WriteLine(element);
        // }
        for(int i = 0;i < ans.Length; i++){
            System.Console.Write(ans[i]);
        }
    }
}
// @lc code=end

