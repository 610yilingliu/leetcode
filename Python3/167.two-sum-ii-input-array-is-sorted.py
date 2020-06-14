#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers, target):
        i = 0
        j = len(numbers) - 1
        if numbers[0] + numbers[-1] == target:
            return [1, j + 1]
        if numbers[0] + numbers[-1] > target:
            while i < j:
                while i < j and numbers[i] + numbers[j] > target:
                    j -= 1
                while i < j and numbers[i] + numbers[j] < target:
                    i += 1
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        if numbers[0] + numbers[-1] < target:
            while i < j:
                while i < j and numbers[i] + numbers[j] < target:
                    i += 1
                while i < j and numbers[i] + numbers[j] > target:
                    j -= 1
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]

            

if __name__ == '__main__':
    a = Solution()
    b = a.twoSum([12,13,23,28,43,44,59,60,61,68,70,86,88,92,124,125,136,168,173,173,180,199,212,221,227,230,277,282,306,314,316,321,325,328,336,337,363,365,368,370,370,371,375,384,387,394,400,404,414,422,422,427,430,435,457,493,506,527,531,538,541,546,568,583,585,587,650,652,677,691,730,737,740,751,755,764,778,783,785,789,794,803,809,815,847,858,863,863,874,887,896,916,920,926,927,930,933,957,981,997], 542)
    print(b)
# @lc code=end

