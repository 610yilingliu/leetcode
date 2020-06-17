/*
 * @lc app=leetcode id=7 lang=csharp
 *
 * [7] Reverse Integer
 */

// @lc code=start
public class Solution {
    public int Reverse(int x) {
        if(x == 0 || x == int.MinValue) return 0;
        int ans = 0;
        int pre_overflow = int.MaxValue / 10;
        int suf_overflow = int.MaxValue % 10;
        bool neg_tag = false;
        if(x < 0){
            neg_tag = true;
        }
        // return directly if x == 0
        x = Math.Abs(x);
        while(x > 0){
            int res = x % 10;
            // if the current answer > int.MaxValue % 10, in the following step, ans = ans * 10, it will cause overflow
            if(ans > pre_overflow) return 0;
            // if answer == int.MaxValue // 10, check the comming digit.
            if(ans == pre_overflow && res > suf_overflow) return 0;
            ans = ans * 10 + res;
            x = x / 10;
        }
        if(neg_tag == true){
            return -ans;
        }
        else return ans;
    }
}
// @lc code=end

