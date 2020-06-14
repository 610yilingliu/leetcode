#
# @lc app=leetcode id=406 lang=python3
#
# [406] Queue Reconstruction by Height
#

# @lc code=start
class Solution:
    def reconstructQueue(self, people):
        people.sort(key = lambda x :(-x[0], x[1]))
        ans = []
        for item in people:
            ans.insert(item[1], item)
        return ans

if __name__ == '__main__':
    a = Solution()
    b = a.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
    print(b)

# @lc code=end

