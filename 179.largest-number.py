#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#

# @lc code=start
class compare(str):
    def __lt__(x, y):
        return x+y > y+x


class Solution:
    def largestNumber(self, nums):

        largest = sorted([str(v) for v in nums], key=compare)  # 排序
        largest = ''.join(largest)  # 转换字符串

        return '0' if largest[0] == '0' else largest 
        
   
# @lc code=end

if __name__ == '__main__':
    a = Solution()
    b = a.largestNumber([10,2])
    print(b)  