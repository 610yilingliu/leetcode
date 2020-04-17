#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start

class Solution:
    def summaryRanges(self, nums):
        nums = nums[::-1]
        head = None
        other = None
        ans = []
        while nums:
            if head == None:
                head = nums.pop()
            elif other == None:
                temp = nums.pop()
                if temp > head + 1:
                    ans.append(str(head))
                    head = temp
                else:
                    other = temp
            else:
                temp = nums.pop()
                if temp > other + 1:
                    ans.append(str(head) + '->' + str(other))
                    other = None
                    head = temp
                else:
                    other = temp
        if head is not None and other is not None:
            ans.append(str(head) + '->' + str(other))
        elif head is not None:
            ans.append(str(head))
        return ans
                    
if __name__ == '__main__':
    a = Solution()
    b = a.summaryRanges([0])
    print(b)
# @lc code=end

