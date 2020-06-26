/*
 * @lc app=leetcode id=507 lang=csharp
 *
 * [507] Perfect Number
 */

// @lc code=start
public class Solution {
    public bool CheckPerfectNumber(int num) {
        if(num < 2) return false;
        int cur = 2;
        int addup = 1;
        while(cur * cur <= num){
            if(num % cur == 0){
                if(cur * cur < num){
                addup += cur;
                addup += num / cur;
                }
                else{
                    addup += cur;
                }
            }
            cur ++;
        }
        return addup == num;
    }
}
// @lc code=end

