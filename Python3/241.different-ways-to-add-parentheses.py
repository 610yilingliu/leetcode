#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#

# @lc code=start
class Solution:
    def diffWaysToCompute(self, input):
        string = input
        nums  = []
        ops = []
        self.ans = dict()
        operators = {'+', '-', '*', '/'}
        i = 0
        while i < len(string):
            num_storage = ''
            while i < len(string) and string[i].isdigit():
                num_storage += string[i]
                i += 1
            if num_storage:
                nums.append(num_storage)
            if i < len(string):
                if string[i] in operators:
                    ops.append(string[i])
                    i += 1
        self.recursion(nums, ops)
        return self.ans.values()
        
    def recursion(self, nums, ops):
        if ops:
            for i in range(len(ops)):
                self.recursion(nums[: i] + ['(' + nums[i] + ops[i] + nums[i + 1] + ')'] + nums[i + 2:], ops[:i] + ops[i + 1:])
        elif nums[0] not in self.ans:
            self.ans[nums[0]] = eval(nums[0])

if __name__ == '__main__':
    a = Solution()
    b = a.diffWaysToCompute("2-1-1")
    print(b)


# @lc code=end

