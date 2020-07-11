/*
 * @lc app=leetcode id=540 lang=csharp
 *
 * [540] Single Element in a Sorted Array
 */

// // @lc code=start
// public class Solution {
//     public int SingleNonDuplicate(int[] nums) {
//         for(int i = 0; i < nums.Length; i += 2){
//             try{
//                 if((nums[i] ^ nums[i + 1]) != 0) return nums[i];
//             }
//             catch{
//                 return nums[nums.Length - 1];
//             }
//         }
//         return -1;
//     }
// }
public class Solution {
    public int SingleNonDuplicate(int[] nums) {
        if(nums.Length == 1) return nums[0];
        int l = 0;
        int r = nums.Length - 1;
        while(l <= r){
            if(r == l) return nums[l];
            int mid = l + (r - l)/2;
            if(nums[mid] == nums[mid + 1]){
                if(((mid -l) & 1) == 1){
                    r = mid - 1;
                }
                else{
                    l = mid;
                }
            }
            else{
                if(((mid -l) & 1) == 1){
                    l = mid + 1;
                }
                else{
                    r = mid;
                }
            }
        }
        return -1;
    }
}
// @lc code=end

