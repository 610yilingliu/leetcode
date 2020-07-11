/*
 * @lc app=leetcode id=416 lang=c
 *
 * [416] Partition Equal Subset Sum
 */

// @lc code=start
int cmp(const void *a, const void *b){
    return *(int *)a < *(int *)b;
}

int sum(int* nums, int numsSize){
    int s = 0;
    for(int i = 0; i < numsSize; i ++){
        s += nums[i];
    }
    return s;
}
int findmax(int* nums, int numsSize){
    int max = 0;
    for(int i = 0; i < numsSize; i ++){
        if(max < nums[i]) max = nums[i];
    }
    return max;
}

int dfs(int target, int curpos, int* nums, int numsSize){
    if(target < 0) return 0;
    if(target == 0) return 1;
    for(int i = curpos; i < numsSize; i ++){
        if(dfs(target - nums[i], i + 1, nums, numsSize) == 1) return 1;
    }
    return 0;
}
bool canPartition(int* nums, int numsSize){
    int s = sum(nums, numsSize);
    if(s % 2 != 0) return 0;
    int max_num = findmax(nums, numsSize);
    int target = s >> 1;
    if(max_num > target) return 0;
    qsort(nums, numsSize, sizeof(int), cmp);
    return dfs(target, 0, nums, numsSize);

}


// @lc code=end

