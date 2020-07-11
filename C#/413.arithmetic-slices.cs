/*
 * @lc app=leetcode id=413 lang=csharp
 *
 * [413] Arithmetic Slices
 */

// @lc code=start
public class Solution {
    public int NumberOfArithmeticSlices(int[] A) {
        if(A is null || A.Length < 3) return 0;
        int ans = 0;
        int pregap = A[1] - A[0];
        int counter = 2;
        for(int i = 1; i <A.Length - 1; i ++){
            if(A[i + 1] - A[i] == pregap) counter ++;
            else{
                if(counter >= 3){
                    for(int c = 3; c <= counter; c++){
                        ans += counter - c + 1;
                    }
                }
                counter = 2;
                pregap = A[i + 1] - A[i];
            }
        }
        if(counter >= 3){
            for(int c = 3; c <= counter; c++){
                ans += counter - c + 1;
            }
        }
        return ans;
    }
}

// public class Solution {
//     public int NumberOfArithmeticSlices(int[] A) {
//         if(A is null || A.Length < 3) return 0;
//         int ans = 0;
//         int pregap = A[1] - A[0];
//         int counter = 2;
//         for(int i = 1; i <A.Length - 1; i ++){
//             int curgap = A[i + 1] - A[i];
//             if(curgap == pregap){
//                 counter ++;
//                 if(counter > 2){
//                     ans += counter - 2;
//                 }
//             }
//             else{
//                 counter = 2;
//                 pregap = curgap;
//             }
//         }
//         return ans;
//     }
// }
// @lc code=end

