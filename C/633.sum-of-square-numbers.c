/*
 * @lc app=leetcode id=633 lang=c
 *
 * [633] Sum of Square Numbers
 */

// @lc code=start


bool judgeSquareSum(int c){
    if(c == 1 || c == 0) return 1;
    (long) c;
    long right = (int)sqrt(c);
    long left = 0;
    while(left <= right){
        long cur = left * left + right * right;
        if(cur < c) left ++;
        else if(cur > c) right --;
        else return 1;
    }
    return 0;
}
// @lc code=end

