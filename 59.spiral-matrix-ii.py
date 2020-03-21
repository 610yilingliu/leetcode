#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n):
        if n == 0 or n == 1:
            return [[1]]
        mat_base = [[0] * n]
        # generate an empty matrix
        for i in range(1, n):
            mat_base += [[0] * n]
        self.ans = mat_base
        nums = []
        for i in range(n**2):
            nums.append(i + 1)
        self.helper(self.ans, 0, nums)
        return self.ans

    def helper(self, current_matrix, time, nums):
        if not nums:
            return
        for i in range(len(current_matrix[0]) - 2 * time):
            self.ans[time][time + i] = nums.pop(0)
        for i in range(len(current_matrix) - 1 - 2* time):
            self.ans[time + i + 1][-1-time] = nums.pop(0)
        for i in range(len(current_matrix[-1]) - 2 * time - 1):
            self.ans[-1 - time][-1 - time - i - 1] = nums.pop(0)
        for i in range(len(current_matrix) - 2 - 2*time):
            self.ans[-1 - time - i - 1][time] = nums.pop(0)
        time = time + 1
        self.helper(current_matrix, time, nums)

# @lc code=end

