/*
 * @lc app=leetcode id=509 lang=csharp
 *
 * [509] Fibonacci Number
 */

// @lc code=start
public class Solution {
    public int Fib(int N) {
        if(N < 2) return N;
        int a = 0;
        int b = 1;
        int c = 0;
        int time = 1;
        while(time < N){
            c = a + b;
            a = b;
            b = c;
            time ++;
        }
        return c;
    }
}
// @lc code=end

