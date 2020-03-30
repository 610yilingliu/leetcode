#
# @lc app=leetcode id=455 lang=python3
#
# [455] Assign Cookies
#

# @lc code=start
class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        # g: children, s:cookies
        count = 0
        i = 0
        j = 0
        while i < len(s) and j < len(g):
            if s[i] >= g[j]:
                count += 1
                i += 1
                j += 1
            else:
                i += 1
        return count

if __name__ == '__main__':
    a = Solution()
    b = a.findContentChildren([1,2], [1,2,3])
    print(b)

# @lc code=end

