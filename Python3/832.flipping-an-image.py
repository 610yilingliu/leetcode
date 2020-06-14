#
# @lc app=leetcode id=832 lang=python3
#
# [832] Flipping an Image
#

# @lc code=start

class Solution:
    def flipAndInvertImage(self, A):
        ans = []
        for item in A:
            inside = []
            item.reverse()
            for digit in item:
				# bitwise method ,equal to inside.append(1 - digit) in this problem
                inside.append(digit ^ 1)
            ans.append(inside)
        return ans




# @lc code=end

