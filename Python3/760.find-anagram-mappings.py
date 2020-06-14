#
# @lc app=leetcode id=760 lang=python3
#
# [760] Find Anagram Mappings
#

# @lc code=start
class Solution:
    def anagramMappings(self, A, B):
        mp = dict()
        # equal to for i in range(len(B)): mp[B[i]] = i
        for idx, num in enumerate(B):
            mp[num] = idx
        ans = []
        for item in A:
            ans.append(mp[item])
        return ans
# @lc code=end

