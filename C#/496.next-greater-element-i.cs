/*
 * @lc app=leetcode id=496 lang=csharp
 *
 * [496] Next Greater Element I
 */

// @lc code=start
public class Solution {
    public int[] NextGreaterElement(int[] nums1, int[] nums2) {
        if (nums1.Length == 0)
            return new int[] { };
        var result = new int[nums1.Length];
        var stack = new Stack<int>();
        var list = nums1.ToList();

        for(int i = 0; i < nums2.Length; i++)
        {
            if(i < result.Length && result[i] == 0 )
                result[i] = -1;
            while(stack.Count > 0 && nums2[i] > nums2[stack.Peek()])
            {
                int idx = list.IndexOf(nums2[stack.Peek()]);
                if(idx > -1)
                    result[idx] = nums2[i];
                stack.Pop();
            }
            stack.Push(i);
        }
        return result;
    }
}
// @lc code=end

