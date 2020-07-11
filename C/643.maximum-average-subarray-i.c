/*
 * @lc app=leetcode id=643 lang=c
 *
 * [643] Maximum Average Subarray I
 */

// @lc code=start


double findMaxAverage(int* nums, int numsSize, int k){
    int sum = 0;
    for(int i = 0; i < k; i ++){
        sum += nums[i];
    }
    int max = sum;
    for(int i = k; i < numsSize; i ++){
        sum = sum - nums[i - k];
        sum = sum + nums[i];
        if(sum > max) max = sum;
    }
    double ans = max/(double)k;
    return ans;
}
// @lc code=end

